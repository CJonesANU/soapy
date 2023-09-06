import soapy
import numpy as np
import matplotlib.pyplot as plt

path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/conf/TestTeleControl.yaml"
sim = soapy.Sim(path)
sim.config.sim.verbosity = 3


print("STARTING AOINIT")

print("=========================\n"*3)
print(sim.config.telCon.type)
print("=========================\n"*3)


sim.aoinit()
sim.makeIMat()
sim.aoloop()

# print(sim.config.telControl.type)