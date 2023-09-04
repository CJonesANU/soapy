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

        self.soapyConfig = soapyConfig # This is a confParse.py:YAML_Configurator object
        self.telVar  = self.soapyConfig.tte.telVar # THIS Calls the confParse attributes
        self.telFreq = self.soapyConfig.tte.telFreq
        self.fsmVar  = self.soapyConfig.tte.fsmVar
        self.fsmFreq = self.soapyConfig.tte.fsmFreq
        self.transmitVar  = self.soapyConfig.tte.transmitVar
        self.transmitFreq = self.soapyConfig.tte.transmitFreq
        self.telError = (0,0)
        self.fsmError = (0,0)

        # Calculated attributes
        self.periods = (1./self.telFreq, 1./self.fsmFreq, 1./self.transmitFreq )
        self.timeSet = np.array( (time.time(),time.time(),time.time() ) ) # This tracks when fsm and tel were last updated

    def __str__(self):
        return "TelVar: " + str(self.telVar) + "\nTelFreq: " + str(self.telFreq) + "\nFSMVar: " + str(self.fsmVar) + "\nFSMFreq: " + str(self.fsmSamp)

    def sampleTel(self):
        # Sample the TelVar
        self.telError += np.random.normal(0, self.telVar,2)
        return
    
    def sampleFSM(self):
        # Sample the FSMVar
        self.fsmError = np.random.normal(0, self.fsmVar,2)
        return
    def sampleTransmit(self):
        self.transmitError = np.random.normal(0,self.transmitVar,2)

    def checkTime(self):
        # Get time now
        now = time.time()
        # Calculate the time delta
        delta = now - self.timeSet
        flags = delta > self.periods
        self.timeSet = self.timeSet*~flags + flags*now  #Use flags as a mask to choose which elements to update
        if flags[0]:
            self.sampleTel()
        if flags[1]:
            self.sampleFSM()
        if flags[2]:
            self.sampleTransmit()
        return flags

    def updateTT(self): # Update both at the same time // maybe not so useful
        flags = self.checkTime()
        return self.telError + self.fsmError

    def updateFSM(self):
        flags = self.checkTime()
        return self.fsmError
    
    def updateTel(self):
        flags = self.checkTime()
        return self.telError
    def updateTransmit(self):
        flags = self.checkTime()
        return self.transmitError
        

    
    
    
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

