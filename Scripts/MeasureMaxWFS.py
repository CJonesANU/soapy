'''
Multithread simulations using Active Object Design Pattern

'''
import threading
import time
import soapy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aotools
import datetime


class SimulationActiveObject(threading.Thread):
    def __init__(self, name: str, args=None):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.result = None

    def run(self):
        print("Starting " + self.name)
        path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/conf/MeasureMaxWFSSim.yaml"
        sim = soapy.Sim(path)
        sim.config.sim.verbosity = 2

        # Programatically change attributes
        if self.args is not None:
            for key, value in self.args.items():
                setattr(sim.config.tte, key, value)

        # dateAndTimeString = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        simName = "./Data/"+self.name 
        sim.config.sim.simName = simName
        sim.aoinit()
        sim.makeIMat(forceNew=False) # Stops them from trying to use the same file
        sim.aoloop()
        self.result = sim

        print("Exiting " + self.name)
    
    def processResults(self):
        measurements = {"stdTT": np.std(self.result.allDmCommands), 
                        "maxTT": np.max(np.abs(self.result.allDmCommands)),
                        "listWfs": self.result.allSlopes,
                        "stdWfs": np.std(self.result.slopes), 
                        "maxWfs": np.max(np.abs(self.result.slopes)),
                        "instStrehl": np.mean(self.result.instStrehl),
                        "longStrehl": self.result.longStrehl[-1][-1],
                        "encircledArea": aotools.image_processing.psf.encircled_energy(self.result.sciImgs[0])
                        }

        return measurements
                        
    def get_result(self):
        return self.result


def plotResults(measurements: list):

    fig, ax = plt.subplots(1,1)
    meanSlopes = np.zeros(len(measurements[0]["listWfs"]))
    for measurement in measurements:
        slopes = measurement["listWfs"]
        # Calc l2 norm slope
        slope = np.sqrt(np.sum(slopes**2, axis=1))
        # Calc cumulative max slope
        for i,s in enumerate(slope):
            if i == 0:
                maxSlope = s
            else:
                maxSlope = max(maxSlope, s)
            slope[i] = maxSlope

        meanSlopes += slope
        ax.plot(slope, color="black", linewidth="0.5")

    meanSlopes /= len(measurements)
    plt.plot(meanSlopes, color="red", linewidth="3")
    plt.title("Cumulative Max Slope")
    plt.xlabel("Iterations")
    plt.ylabel("L2 Norm Slope")
    plt.text(0.8,0.2, "telVar=100,\ntelFreq=15 \nrandom Walk \nmaxStroke=10", transform=ax.transAxes)
    plt.show()


def main():
    nObjects = 3
    # List of variances to use
    measurements = []

    for i in range(5):
        activeObjects = []
        for j in range(nObjects):
            activeObjects.append(SimulationActiveObject("Thread-" + str(j) ) )
                                
        # Start the threads
        for activeObject in activeObjects:
            activeObject.start()

        # Wait for all threads to complete
        for activeObject in activeObjects:
            activeObject.join()
        # Get the results
        for j,activeObject in enumerate(activeObjects):
            measurements.append(activeObject.processResults())
    
    print(measurements[0]["maxTT"])
    print(measurements[1]["maxTT"])
    plotResults(measurements)
    # print(measurements.shape)
    # print(measurements)
    # # plotResults(measurements)
    # slopes = measurements["listWfs"]
    # plt.plot(np.sqrt(np.sum(slopes**2, axis=1)))
    # plt.show()



if __name__ == "__main__":
    main()