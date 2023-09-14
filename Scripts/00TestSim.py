'''
Quick Test to make sure that soapy is working

'''
import soapy
import numpy as np
import matplotlib.pyplot as plt
import aotools


# Show resulting science cam and first phase screen
# Generate 1 x 2 sub plot figure

# Create a simulation object
path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/conf/RandomScrns.yaml"
sim = soapy.Sim(path)


# init the simulation
sim.aoinit()
# sim.config.sim.nIters = 20
sim.makeIMat(forceNew=True)
sim.aoloop()

fig, ax = plt.subplots(4,1)
ax[0].plot(sim.allDmCommands)
ax[2].plot(sim.allSlopes)
ax[1].plot(sim.allTelPos)
ax[3].plot(sim.allSlewrates)
# Add titles to each subplot
ax[0].set_title("DM Commands")
ax[2].set_title("Slopes")
ax[1].set_title("Telescope Position")
ax[3].set_title("Slew Rates")
plt.show()
