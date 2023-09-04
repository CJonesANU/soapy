'''
Loop through a range of TT Variance values, and plot the Strehl Ratio vs TT Variance
'''

import soapy
import numpy as np
import matplotlib.pyplot as plt

# Create a simulation object
configFile = "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/conf/OCGS.yaml"
sim = soapy.Sim(configFile)

# Create array of FSM Variance values to loop through
ttVars = np.linspace(0, 1200, 10)

# Create array to store Strehl Ratios
strehlRatios = np.zeros(len(ttVars))

# Loop through FSM Variance values
for i, fsmVar in enumerate(ttVars):
    # Set FSM Variance
    sim.config.tte.fsmVar = fsmVar
    sim.config.tte.telVar = fsmVar
    sim.config.sim.nIters = 1
    sim.aoinit()

    # init the simulation
    # Run AO Loop
    sim.makeIMat()
    sim.aoloop()
    # Store Strehl Ratio
    strehlRatios[i] = sim.longStrehl[0][-1]


# Plot Strehl Ratio vs FSM Variance
plt.plot(ttVars, strehlRatios)
plt.title("Strehl Ratio vs TT Variance")
plt.xlabel("TT Variance")
plt.ylabel("Strehl Ratio")
plt.show()