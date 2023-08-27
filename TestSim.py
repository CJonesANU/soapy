'''
Quick Test to make sure that soapy is working

'''
import soapy
import numpy as np
import matplotlib.pyplot as plt


# Show resulting science cam and first phase screen
# Generate 1 x 2 sub plot figure
fig, ax = plt.subplots(2,2)

# Create a simulation object
configFile = "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/conf/OCGSSMF.yaml"
sim = soapy.Sim(configFile)
# init the simulation
sim.aoinit()

# sim.config.sim.nIters = 50
sim.makeIMat()
sim.aoloop()


# Plot Phase Screen Used
ax[0,0].imshow(sim.scrns[0])
ax[0,0].set_title("Phase Screen Used")
# Show Science Camera Image 
ax[1,0].imshow(sim.sciImgs[0])
ax[1,0].set_title("Science Camera Image")

# Now set TTError to 0
sim.config.tte.fsmVar = 0
sim.config.tte.telVar = 0

sim.aoinit()
sim.makeIMat()
sim.aoloop()

# Plot Phase Screen Used
ax[0,1].imshow(sim.scrns[0])
ax[0,1].set_title("Phase Screen Used")
# Show Science Camera Image 
ax[1,1].imshow(sim.sciImgs[0])
ax[1,1].set_title("Science Camera Image")
# Add color bar
plt.show()
