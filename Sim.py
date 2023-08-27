'''
Author: Cameron Jones

Run Soapy Simulation with TT Error, for a given number of iterations
Plot the Strehl Ratio
'''
import soapy
import numpy as np
import matplotlib.pyplot as plt

# Create a simulation object
configFile = "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/conf/OCGSSMF.yaml"
sim = soapy.Sim(configFile)
# init the simulation
sim.aoinit()


# Create array to store Strehl Ratios
strehlRatios = np.zeros(sim.config.sim.nIters)

# Run AO Loop
sim.makeIMat()
sim.aoloop()

longStrehl = sim.longStrehl[0][0:sim.config.sim.nIters]
instStrehl = sim.instStrehl[0][0:sim.config.sim.nIters]

# Plot Strehl Ratio vs Iteration
plt.plot(longStrehl, label="Long Exposure")
plt.plot(instStrehl, label="Instantaneous")
plt.title("Strehl Ratio vs Iteration")
plt.legend()
plt.xlabel("Iteration")
plt.ylabel("Strehl Ratio")
plt.show(block=False)

plt.imshow(sim.sciImgs[0])
plt.title("Science Image")
plt.show()
