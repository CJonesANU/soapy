'''
Simulate error as a function of frequency
'''
import numpy as np
import matplotlib.pyplot as plt
import soapy
import aotools

# Create a simulation object
configFile = "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/conf/OCGSSMF.yaml"
sim = soapy.Sim(configFile)
# sim.config.sim.nIters = 20
sim.setLoggingLevel(1)

fstart, fend, nsteps = 0.01, 200, 100
frequencies = np.logspace(fstart, fend, nsteps)

instStrehl = np.zeros(nsteps)
longStrehl = np.zeros(nsteps)
fwhmRadii = np.zeros(nsteps)
sim.aoinit()
for i,f in enumerate(frequencies):
    sim.config.tte.fsmFreq = f
    print("====================================")
    print(f"Progress: {i:.2f} of {nsteps:.2f}")

    # init the simulation
    sim.setLoggingLevel(0)
    sim.aoinit()
    sim.makeIMat(forceNew=True)
    sim.aoloop()

    instStrehl[i] = np.mean(sim.instStrehl)
    longStrehl[i] = sim.longStrehl[-1][-1] 
    FWHMRad = aotools.image_processing.psf.encircled_energy(sim.sciImgs[0])
    fwhmRadii[i] = FWHMRad
    sim.reset_loop()
    print("====================================")
    print("MEAN INST STREHL: ", np.mean(sim.instStrehl)   )
    print("Long Strehl: ",      sim.longStrehl[-1][-1]    )
    print("FWHM: ", str(FWHMRad))
    print("====================================")

# Plot the results
fig, ax = plt.subplots(1,3)
ax[0].plot(frequencies, instStrehl,'bo')
ax[0].set_xlabel("Frequency")
ax[0].set_ylabel("Inst Strehl")
ax[0].set_title("Inst Strehl vs Frequency")
ax[1].plot(frequencies, longStrehl,'bo')
ax[1].set_xlabel("Frequency")
ax[1].set_ylabel("Long Strehl")
ax[1].set_title("Long Strehl vs Frequency")
ax[2].plot(frequencies, fwhmRadii,'bo')
ax[2].set_xlabel("Frequency")
ax[2].set_ylabel("FWHM Radius")
ax[2].set_title("FWHM Radius vs Frequency")
plt.show()

# Save them all to a csv file
np.savetxt("instStrehl.csv", instStrehl, delimiter=",")
np.savetxt("longStrehl.csv", longStrehl, delimiter=",")
np.savetxt("fwhmRadii.csv", fwhmRadii, delimiter=",")
np.savetxt("frequencies.csv", frequencies, delimiter=",")




