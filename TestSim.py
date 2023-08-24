'''
Quick Test to make sure that soapy is working
'''
import soapy
import numpy as np
import matplotlib.pyplot as plt

# Create a simulation object
configFile = "./conf/OCGS.yaml"
sim = soapy.Sim(configFile)
# init the simulation
sim.aoinit()
sim.makeIMat()
sim.aoloop()

# Show resulting science cam and first phase screen
# Generate 1 x 2 sub plot figure
fig, ax = plt.subplots(1,2)
# Plot Phase Screen Used
ax[0].imshow(sim.scrns[0])
# Show Science Camera Image 
ax[1].imshow(sim.sciImgs[0])
plt.show()
