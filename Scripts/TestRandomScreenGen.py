
import threading
import time
import soapy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aotools
import datetime
import astropy
import os




path = "conf/RandomScrns.yaml"
sim = soapy.Sim(path)


class SimulationActiveObject(threading.Thread):
    def __init__(self, name: str, args=None):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.result = None

    def run(self):
        print("Starting " + self.name)
        path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/conf/RandomScrns.yaml"
        sim = soapy.Sim(path)
        sim.config.sim.verbosity = 0

        # Programatically change attributes
        for key, value in self.args.items():
            parent, child = key.split('.') #This is a stupid but effective way of accessing nested attributes
            setattr(getattr(sim.config, parent), child, value)

        # dateAndTimeString = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        simName = self.name 
        sim.config.sim.simName += simName
        sim.aoinit()
        sim.makeIMat(forceNew=True) # Stops them from trying to use the same file
        sim.aoloop()
        self.result = sim

        print("Exiting " + self.name)
    
    def processResults(self):
        measurements = {"stdTT": np.std(self.result.allDmCommands), 
                        "maxTT": np.max(np.abs(self.result.allDmCommands)),
                        "stdWfs": np.std(self.result.slopes), 
                        "maxWfs": np.max(np.abs(self.result.slopes)),
                        "encircledArea": aotools.image_processing.psf.encircled_energy(self.result.sciImgs[0])
                        }
        return measurements
                        
    def get_result(self):
        return self.result

class SimulationResults(object):
    def __init__(self, simName):
        self.simName = simName
        measurements = {"stdTT": [],
                        "maxTT": [],
                        "stdWfs": [],
                        "maxWfs": [],
                        "encircledArea": []
                        }
        self.measurements = pd.DataFrame(measurements)
    
    def addMeasurement(self, measurement):
        self.measurements = self.measurements.append(measurement, ignore_index=True)

    def __str__(self):
        return f"{self.simName}: {self.measurements}"

    def __repr__(self):
        return f"{self.simName}: {self.measurements}"

    def processDf(self):
        means = self.measurements.mean()
        stds = self.measurements.std()
        return [means, stds]

    def save(self, path):
        self.measurements.to_csv(path)
    
def generateBlankPhaseScrn(atmosphereParams: dict ) -> str:
    '''
    Generate a blank phase screen of size n x n
    '''
    size = atmosphereParams["size"]
    scrn = np.zeros((size, size))
    path = "conf/Size{}Scrns.fits".format(size)
    astropy.io.fits.writeto(path, scrn, overwrite=True)
    return path

def generateRandomPhaseScrn(atmosphereParams: dict, n: int) -> str:
    '''
    Generate a random phase screen of size n x n
    '''
    size = atmosphereParams["size"]
    r0 = atmosphereParams["r0"]
    L0 = atmosphereParams["L0"]
    pixel_scale = atmosphereParams["pixel_scale"]

    directory = "conf/Size{}Scrns".format(size)
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        print("Creating directory: {}".format(directory))
        os.makedirs(directory)

    for i in range(n):
        scrn = aotools.turbulence.PhaseScreenKolmogorov(size,pixel_scale, r0, L0).scrn
        path = "conf/Size{}Scrns/{}.fits".format(size, i)
        astropy.io.fits.writeto(path, scrn, overwrite=True)
    return directory

def main():
    path = "conf/RandomScrns.yaml"
    nSims = 480
    nObjects = 2
    sim = soapy.Sim(path)

    # Generate Phase Screens
    atmosphereParameters = {"size": 256,
                            "r0": sim.config.atmos.r0, 
                            "L0": sim.config.atmos.L0[0], 
                            "pixel_scale": sim.config.tel.telDiam / sim.config.sim.pupilSize}
    # print(atmosphereParameters)
    print(" Generate Random Phase Screens")
    randomScrnDir = "./"+generateRandomPhaseScrn(atmosphereParameters, nSims)
    print(" Generate Blank Phase Screen")
    blankScrnPath = "./"+generateBlankPhaseScrn(atmosphereParameters)
    results = SimulationResults("telWalkOnly")

    print("=====================================")
    print("Begin Main Loop")

    for j in range(nSims//nObjects): 
        activeObjects = []
        print("=====================================")
        print("Iteration {} of {}".format(j, nSims//nObjects))
        for i in range(nObjects):
            scrnInx = i+j*nObjects
            scrn = randomScrnDir+"/"+str(scrnInx)+".fits"

            print("Simulating with {}".format(scrn))
            scrnPathList = [blankScrnPath, scrn, blankScrnPath]
            object = SimulationActiveObject("RandomScrn"+str(scrnInx), {"atmos.scrnNames": scrnPathList})
            activeObjects.append(object)

    
        for object in activeObjects:
            object.start()
    
 
        for i, object in enumerate(activeObjects):
            object.join()
            results.addMeasurement(object.processResults())

    print(results.measurements)
    means, stds = results.processDf()
    print("=====================================")
    print("Mean of Resutls: ")
    print(means)
    print("=====================================")
    print("Standard Deviation of Results: ")
    print(stds)
    print("=====================================")

    # Save results
    results.save("Results.csv")

    # Plot encircled energy
    plt.hist(results.measurements["encircledArea"], bins=10)
    plt.show()

    # fig, ax = plt.subplots(1,3)
    # ax[0].hist(results.measurements["stdTT"])
    # ax[1].hist(results.measurements["stdWfs"])
    # ax[2].hist(results.measurements["encircledArea"])
    # plt.show()



    



if __name__ == "__main__":
    main()