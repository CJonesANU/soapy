'''
Quick Test to make sure that soapy is working

'''
import soapy
import numpy as np
import matplotlib.pyplot as plt
import aotools


# Show resulting science cam and first phase screen
# Generate 1 x 2 sub plot figure
fig, ax = plt.subplots(2,2)

# Create a simulation object
configFile = "./conf/OCGSSMF.yaml"
sim = soapy.Sim(configFile)
# init the simulation
sim.aoinit()

# sim.config.sim.nIters = 20
sim.makeIMat(forceNew=True)
sim.aoloop()

print("MEAN INST STREHL: ", np.mean(sim.instStrehl)   )
print("Long Strehl: ",      sim.longStrehl[-1][-1]    )
FWHMRad = aotools.image_processing.psf.encircled_energy(sim.sciImgs[0])
print("FWHM: ", str(FWHMRad))
# Plot Phase Screen Used
ax[0,0].imshow(sim.scrns[0])
ax[0,0].set_title("Phase Screen Used")
# Show Scie:wnce Camera Image 
ax[1,0].imshow(sim.sciImgs[0])
ax[1,0].set_title("Science Camera Image")

# # In a second figure, plot all three phase scrns

fig2, ax2 = plt.subplots(1,3)
ax2[0].imshow(sim.scrns[0])
ax2[1].imshow(sim.scrns[1])
ax2[2].imshow(sim.scrns[2])
plt.show()


# # Plot the TT magnitude as a function of iteration
# TT = sim.allDmCommands

# ax[0,1].plot(TT[:,0])
# ax[0,1].plot(TT[:,1])
# ax[0,1].set_title("TT Magnitude")
# ax[0,1].set_xlabel("Iteration")
# ax[0,1].set_ylabel("TT Magnitude")


# # # Now set TTError to 0
# sim.config.tte.fsmVar = 0
# sim.config.tte.telVar = 0

# sim.aoinit()
# sim.makeIMat()
# sim.aoloop()

# # Plot Phase Screen Used
# ax[0,1].imshow(sim.scrns[0])
# ax[0,1].set_title("Phase Screen Used")
# # Show Science Camera Image 
# ax[1,1].imshow(sim.sciImgs[0])
# ax[1,1].set_title("Science Camera Image")
# # Add color bar
plt.show()
