#! /usr/bin/env python3
'''
Vary the variance of Telescope and see how it affects the absolute mean DM shape
'''
import soapy
import numpy as np
import matplotlib.pyplot as plt

# Create a simulation object
configFile = "./conf/OCGSSMF.yaml"
sim = soapy.Sim(configFile)

# List of variances to use
vStart, vEnd, vSteps = 0, 1000, 30
variances = np.linspace(vStart, vEnd, vSteps)

ttMean = []
ttStd = []
wfsMean = []
wfsStd = []
instStrehl = []
longStrehl = []
for i,v in enumerate(variances):
    # Set telescope variance
    sim.config.tte.telVar = v
    # init the simulation
    sim.aoinit()
    sim.makeIMat()
    sim.aoloop()
    # Get the DM commands
    TT = sim.allDmCommands
    # Get the mean DM shape
    meanTT = np.mean(np.abs(TT) )
    stdTT = np.std(TT)
    meanWfs = np.mean(np.abs(sim.slopes))
    stfWfs = np.std(sim.slopes)
    ttMean.append(meanTT)
    ttStd.append(stdTT)
    wfsMean.append(meanWfs)
    wfsStd.append(stfWfs)
    instStrehl.append(np.mean(sim.instStrehl ))
    longStrehl.append(sim.longStrehl[-1])



# Plot the mean DM shape
fig, ax = plt.subplots(1,3) 
ax[0].plot(ttMean,'bo',label="Mean DM Shape")
ax[0].plot(ttStd,'ro',label="STD DM Shape")
ax[0].set_title("DM Shape")
ax[0].legend()
ax[1].plot(wfsMean,'bo',label="Mean WFS Shape")
ax[1].plot(wfsStd,'ro',label="STD WFS Shape")
ax[1].set_title("Slopes")
ax[1].legend()
ax[3].plot(instStrehl, label="Inst Strehl")
ax[3].plot(longStrehl, label="Long Stehl")
ax[3].legend()

plt.show()