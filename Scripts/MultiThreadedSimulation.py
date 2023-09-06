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
        path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/conf/OCGSSMF.yaml"
        sim = soapy.Sim(path)
        sim.config.sim.verbosity = 0

        # Programatically change attributes
        for key, value in self.args.items():
            setattr(sim.config.tte, key, value)

        dateAndTimeString = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        simName = dateAndTimeString +"_"+ self.name 
        sim.config.sim.simName = simName
        sim.aoinit()
        sim.makeIMat(forceNew=False) # Stops them from trying to use the same file
        sim.aoloop()
        self.result = sim

        print("Exiting " + self.name)
    
    def processResults(self):
        measurements = {"stdTT": np.std(self.result.allDmCommands), 
                        "maxTT": np.max(np.abs(self.result.allDmCommands)),
                        "stdWfs": np.std(self.result.slopes), 
                        "maxWfs": np.max(np.abs(self.result.slopes)),
                        "instStrehl": np.mean(self.result.instStrehl),
                        "longStrehl": self.result.longStrehl[-1][-1],
                        "encircledArea": aotools.image_processing.psf.encircled_energy(self.result.sciImgs[0])
                        }
        return measurements
                        
    def get_result(self):
        return self.result




def main():
    nObjects = 12
    activeObjects = []
    telVar = "telVar"
    # List of variances to use
    vStart, vEnd, vSteps = 0, 150, nObjects
    variances = np.linspace(vStart, vEnd, vSteps)
    
    fStart, fEnd, fSteps = 1, 120, 15
    frequencies = np.linspace(fStart, fEnd, fSteps)

    longStrehl = np.zeros((fSteps,nObjects))
    maxTT      = np.zeros((fSteps,nObjects))
    Radii      = np.zeros((fSteps,nObjects))
    maxSlopes  = np.zeros((fSteps,nObjects))

    for i,f in enumerate(frequencies):
        # Create a list of active objectso
        print("=====================================")
        print("Starting frequency: ", f)
        print("=====================================")
        activeObjects = []
        for j,v in enumerate(variances):
            activeObjects.append(SimulationActiveObject("Thread-" + str(j), {"telVar": v, "telFreq": f}) )
        # Start the threads
        for activeObject in activeObjects:
            activeObject.start()
        # Wait for all threads to complete
        for activeObject in activeObjects:
            activeObject.join()
        # Get the results
        for j,activeObject in enumerate(activeObjects):
            measurements = activeObject.processResults()
            longStrehl[i,j] = (measurements["longStrehl"])
            maxTT[i,j] = (measurements["maxTT"])
            Radii[i,j] = (measurements["encircledArea"])
            maxSlopes[i,j] = (measurements["maxWfs"])

    # Plot the results on imshow
    fig, ax = plt.subplots(1,4)
    ax[0].imshow(longStrehl)
    ax[0].set_title("Long Strehl")
    ax[0].set_xlabel("Tel Var")
    ax[0].set_ylabel("Tel Freq")

    ax[1].imshow(Radii)
    ax[1].set_title("Encircled Energy")

    ax[2].imshow(maxTT)
    ax[2].set_title("Max TT")

    ax[3].imshow(maxSlopes)
    ax[3].set_title("Max Slopes")

    # fig.colorbar(ax[0].imshow(longStrehl), ax=ax[0])
    # fig.colorbar(ax[1].imshow(maxTT), ax=ax[1])
    # fig.colorbar(ax[2].imshow(Radii), ax=ax[2])
    
    plt.show()



if __name__ == "__main__":
    main()