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
    def __init__(self, name, sim, args=None):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.result = None

    def run(self):
        print("Starting " + self.name)
        path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/conf/OCGSSMF.yaml"
        sim = soapy.Sim(path)
        sim.config.sim.verbosity = 0

        dateAndTimeString = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        simName = dateAndTimeString + "_TelVarFSMResponse"
        sim.config.sim.simName = simName
        sim.aoinit()
        sim.makeIMat(forceNew=True)
        sim.aoloop()

        self.result = sim.longStrehl[-1][-1]

        print("Exiting " + self.name)

    def get_result(self):
        return self.result

if __name__ == "__main__":
    nObjects = 5
    activeObjects = []
    for n in range(nObjects):
        activeObjects.append(SimulationActiveObject("Thread-" + str(n), soapy.Sim))
        # time.sleep(2) # Wait one seocond before starting the next thread

    # Start all threads without waitign for them to finish
    for activeObject in activeObjects:
        activeObject.start()
        time.sleep(2)

 
    
    # # wait one second
    # time.sleep(1)

    for activeObject in activeObjects:
        activeObject.join()

    for activeObject in activeObjects:
        print(activeObject.get_result())