'''
Telescpe Control Module,

Based of PID Controller
'''
import time
import numpy as np


    # def __init__(self, soapyConfig):

    #     self.soapyConfig = soapyConfig # This is a confParse.py:YAML_Configurator object

    #     self.Kp = self.soapyConfig.telControl.Kp
    #     self.Ki = self.soapyConfig.telControl.Ki
    #     self.Kd = self.soapyConfig.telControl.Kd
        
    #     self.controlFreq = self.soapyConfig.telControl.controlFreq

    #     # Calculated attributes
    #     self.P = (0,0)
    #     self.I = (0,0)
    #     self.D = (0,0)

    #     self.PID = (0,0)

    #     self.error = np.array((0,0))
    #     self.integral =  np.array((0,0))
    #     self.period = 1./self.controlFreq
    #     self.timeset = time.time()
    
    # def __str__(self):
    #     return "Kp: " + str(self.Kp) + "\nKi: " + str(self.Ki) + "\nKd: " + str(self.Kd)


class telescopeController(object):
    def __init__(self,soapyConfig):
        print("INIT BASE")
        self.soapyConfig = soapyConfig
        # print("TEL CONTROL CONFIG")
        # print(self.soapyConfig.telCon)L
        self.controlFreq = self.soapyConfig.telCon.controlFreq

        self.error = np.array((0,0))
        self.period = 1./self.controlFreq
        self.timeset = time.time()
    
    def checkTime(self):
        # Get time now
        now = time.time()
        # Calculate the time delta
        delta = now - self.timeSet
        update = delta > self.period
        return update
    
    def slewRate(self, error):
        """
        This function should be overwritten by the child class
        """
        pass

    def update(self, error):
        if self.checkTime():
            self.timeSet = time.time()
            return self.slewRate(error)
        else:
            return self.slewRate


class telescopeSimpleController(telescopeController):
    def __init__(self, soapyConfig) -> None:
        print("INIT SIMPLE")
        self.soapyConfig = soapyConfig
        self.range = self.soapyConfig.telCon.range
        self.slewRateConstant = self.soapyConfig.telCon.slewRate

    def inRange(self, error):
        flags = [0,0]
        for i, e in enumerate(error):
            if e > self.range:
                flags[i] = 1
            elif e < -self.range:
                flags[i] = -1
            else:
                flags[i] = 0
        return np.array(flags)
    
    def slewRate(self,error):
        self.slewRate = self.inRange(error)*self.slewRateConstant
        return self.slewRate




class telescopePidController(telescopeController):


    def __init__(self, soapyConfig):
        print("INIT PID")

        self.Kp = self.soapyConfig.telCon.Kp
        self.Ki = self.soapyConfig.telCon.Ki
        self.Kd = self.soapyConfig.telCon.Kd
        

        # Calculated attributes
        self.P = (0,0)
        self.I = (0,0)
        self.D = (0,0)

        self.integral =  np.array((0,0))
    

    def slewRate(self, error: np.ndarray):
        
        self.P = self.Kp*error
        
        self.integral += error
        self.I = self.Ki*self.integral
        
        self.D = self.Kd*(error - self.error)
        
        self.error = error
        self.slewRate = self.P + self.I + self.D
        return self.slewRate
    