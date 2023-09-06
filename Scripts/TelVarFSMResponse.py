#! /usr/bin/env python3
'''
Vary the variance of Telescope and see how it affects the absolute mean DM shape
'''
import soapy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aotools
import datetime

# Create a pandas dataframe to store the data, columns are:
# [stdTT, meanWfs, stfWfs, instStrehl, longStrehl]
# Indexed by the variance


def CollectData(sim: soapy.Sim, Results: pd.DataFrame, variance: float):
    # Get the DM commands
    TT = sim.allDmCommands
    # Get the mean DM shape
    stdTT = np.std(TT)
    maxTT = np.max(np.abs(TT))
    stdWfs = np.std(sim.slopes)
    maxWfs = np.max(np.abs(sim.slopes))
    instStrehl = np.mean(sim.instStrehl )
    longStrehl = sim.longStrehl[-1][-1]
    encircled_energy = aotools.image_processing.psf.encircled_energy(sim.sciImgs[0])
    # Add to the dataframe
    Results.loc[variance] =    [ stdTT,  maxTT,   stdWfs,  maxWfs,   instStrehl,   longStrehl,  encircled_energy]
    return  Results                                                                                             
Results = pd.DataFrame(columns=["stdTT","maxTT", "stdWfs","maxWfs", "instStrehl", "longStrehl","encircledArea"])

# Create a simulation object
configFile = "./conf/OCGSSMF.yaml"
sim = soapy.Sim(configFile)
# Rename the simulation so it goes into a new folder. 
# Name it after the Current Date and Time
dateAndTimeString = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
simName = dateAndTimeString + "_TelVarFSMResponse"
sim.config.sim.simName = simName


# Set the verbosity to 0
# sim.config.sim.verbosity = 0

# List of variances to use
vStart, vEnd, vSteps = 0, 150, 15
variances = np.linspace(vStart, vEnd, vSteps)

for i,v in enumerate(variances):
    print("-----------------------------------")
    print("Iteration: ", i, " of ", len(variances))
    print("-----------------------------------")
    # Set telescope variance
    sim.config.tte.telVar = v
    print("Sim Begin")
    # init the simulation
    sim.aoinit()
    sim.makeIMat(forceNew=True)
    sim.aoloop()
    print("Finished Simulation: Now begin Data Analysis")
    # Collect the data
    Results = CollectData(sim, Results, v)
    print("Data Analysis complete, next loop")
    print("-----------------------------------")

# Save Dataframe for later use
Results.to_csv("TelVarianceResults.csv")