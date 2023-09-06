import soapy
import numpy as np
import matplotlib.pyplot as plt

path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/conf/TestTeleControl.yaml"
sim = soapy.Sim(path)
sim.config.sim.verbosity = 3


print("STARTING AOINIT")
sim.aoinit()

# print(sim.config.telControl.type)