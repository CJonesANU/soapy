import soapy
import numpy as np
import matplotlib.pyplot as plt

path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/conf/TestTeleControl.yaml"
sim = soapy.Sim(path)
sim.config.sim.verbosity = 2


print("STARTING AOINIT")

# print("=========================\n"*3)
# print(sim.config.telCon.type)
# print("=========================\n"*3)

sim.aoinit()
sim.makeIMat()
sim.aoloop()

slopes = sim.allSlopes
tt = sim.allDmCommands
telPos = sim.allTelPos

fig, ax = plt.subplots(3,1)
ax[0].plot(tt)
ax[0].set_title("DM Commands")
# Set y axis between +1 and -1
# ax[0].set_ylim([-1,1])
ax[1].plot(slopes)
ax[1].set_title("Slopes")
# Set y axis between +1 and -1
ax[1].set_ylim([-1,1])
ax[2].plot(telPos)
ax[2].set_title("TelPos")
# Set y axis between +1 and -1
# ax[2].set_ylim([-1,1])


plt.show()



# print(sim.config.telControl.type)