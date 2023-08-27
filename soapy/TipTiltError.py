"""
Tip-Tilt Error Injector
=======================
This module simulates the error associated with pointing the telescope and FSM, (and maybe the downlink terminal).
It does this by injecting Tip-Tilt error into the wavefront during the simulation.
TT error will be modelled by the sum of normal distributions for both elements, samples at different rates.
"""

import numpy as np
import matplotlib.pyplot as plt
import soapy
import yaml
import aotools
import time


class TipTiltError(object):
    def __init__(self, soapyConfig):
        # print("Initializing TipTiltError")
        # # Read TelVar, TelFreq, FSMVar, FSMSamp from config file
        # # Open config yaml file
        # print("Reading config file: ", config_path)
        # with open(config_path, 'r') as yaml_file:
        #     config = yaml.safe_load(yaml_file)

        # # Access the parameters using dictionary-like syntax
        # self.telVar  = config['TelVar']
        # self.telFreq = config['TelFreq']
        # self.fsmVar  = config['FSMVar']
        # self.fsmSamp = config['FSMFreq']
        # self.time = time.time()
        # self.telError = 0
        # self.fsmError = 0
        # print("Done Initializing TipTiltError")

        self.soapyConfig = soapyConfig # This is a confParse.py:YAML_Configurator object
        self.telVar  = self.soapyConfig.tte.telVar # THIS Calls the confParse attributes
        self.telFreq = self.soapyConfig.tte.telFreq
        self.fsmVar  = self.soapyConfig.tte.fsmVar
        self.fsmFreq = self.soapyConfig.tte.fsmFreq
        self.time = time.time()-10 #Hack to get everythging to run the first time
        self.telError = (0,0)
        self.fsmError = (0,0)



    def __str__(self):
        return "TelVar: " + str(self.telVar) + "\nTelFreq: " + str(self.telFreq) + "\nFSMVar: " + str(self.fsmVar) + "\nFSMFreq: " + str(self.fsmSamp)

    
    def sampleTel(self):
        # Sample the TelVar
        self.telError = np.random.normal(0, self.telVar,2)
        return
    
    def sampleFSM(self):
        # Sample the FSMVar
        self.fsmError = np.random.normal(0, self.fsmVar,2)
        return

    def timeDelta(self):
        # Get time now
        now = time.time()
        # Calculate the time delta
        delta = np.abs(now - self.time)
        # Update the time
        self.time = now
        return delta

    def updateTT(self): # Update both at the same time // maybe not so useful
        # Check if it is time to update the TT error
        Delta = self.timeDelta()
        if Delta > 1./self.telFreq:
            # Update the TelVar
            self.sampleTel()
        if Delta > 1./self.fsmFreq:
            # Update the FSMVar
            self.sampleFSM()
        return self.telError + self.fsmError

    def updateFSM(self):
        Delta = self.timeDelta()
        if Delta > 1./self.fsmFreq:
            # Update the FSMVar
            self.sampleFSM()
            print("UPDATED FSMError: ", self.fsmError)
            return self.fsmError
        else:
            print("FSMError: ", self.fsmError)
            return self.fsmError
    
    def updateTel(self):
        Delta = self.timeDelta()
        if Delta > 1./self.telFreq:
            # Update the TelVar
            self.sampleTel()
            return self.telError
        else:
            return self.telError
        

    
    
    
# # Test Class
# if __name__ == "__main__":
#     # Create TipTiltError object
#     tte = TipTiltError("/home/cameron/Documents/projects/SOAPY_TTError/soapy/conf/TTError.yaml")
#     # Print out the config
#     print(tte)

#     # Sample the TelVar
#     tte.sampleTel()
#     print("TelError: ", tte.telError)
#     # Sample the FSMVar
#     tte.sampleFSM()
#     print("FSMError: ", tte.fsmError)

#     # Wait one second
#     time.sleep(1)
#     tte.updateTT()
#     print("TelError: ", tte.telError)
#     print("FSMError: ", tte.fsmError)

#     print("Error: ", tte.updateTT())

