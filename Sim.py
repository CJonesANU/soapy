'''
Author: Cameron Jones

Run Soapy Simulation with TT Error, for a given number of iterations
Plot the Strehl Ratio
'''
import soapy
import numpy as np
import matplotlib.pyplot as plt

# Create a simulation object
configFile = "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/conf/OCGS.yaml"
sim = soapy.Sim(configFile)
# init the simulation
sim.aoinit()

# Set number of iterations
sim.config.sim.nIters = 35

# Create array to store Strehl Ratios
strehlRatios = np.zeros(sim.config.sim.nIters)

# Run AO Loop
sim.makeIMat()
sim.aoloop()

print("Number of Images: ", len(sim.sciImgs))

# Analyse Strehl Ratio for Science Camera Images
for i in range(len(sim.sciImgs)):
    strehlRatios[i] = sim.sciImgs[i].max()/sim.sciImgs[i].mean()
plt.plot(strehlRatios)
plt.title("Strehl Ratio vs Iteration")
plt.xlabel("Iteration")
plt.ylabel("Strehl Ratio")
plt.show()