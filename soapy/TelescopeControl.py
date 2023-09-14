'''
Telescpe Control Module,

Based of PID Controller
'''
import time
import numpy as np


class telescopeController(object):
    def __init__(self,soapyConfig):
        self.soapyConfig = soapyConfig
        # print("TEL CONTROL CONFIG")
        # print(self.soapyConfig.telCon)
        self.controlFreq = self.soapyConfig.telCon.controlFreq
        self.jitter = self.soapyConfig.telCon.jitter
        
        self.slewRate = np.array((0.0,0.0))
        self.dt = self.soapyConfig.sim.loopTime
        self.Pos = np.array((0.0,0.0))
        self.error = np.array((0.0,0.0))
        self.period = 1./self.controlFreq
        # print("SETTING TIME IN telescopeController")
        self.timeSet = time.time()
        # print("telescopeController INIT COMPLETE")
    
    def checkTime(self):
        # Get time now
        now = time.time()
        # Calculate the time delta
        delta = now - self.timeSet
        update = delta > self.period
        return update
    
    def calcSlewRate(self, error):
        """
        This function should be overwritten by the child class
        """
        pass

    def updatejitter(self):
        """
        This function does the jitter for the telescope, replacing TTE module method
        """
        dE = np.random.normal(0, self.jitter,2)
        self.Pos += dE

    def update(self, error):
        if self.checkTime():
            self.timeSet = time.time()
            self.calcSlewRate(error)
            self.Pos -= self.slewRate*self.dt
            self.updatejitter()
            return self.Pos
        else:
            self.Pos -= self.slewRate*self.dt
            return self.Pos


class telescopeSimpleController(telescopeController):
    def __init__(self, soapyConfig) -> None:
        super().__init__(soapyConfig)
        # print("Start telescopeSimpleController INIT")
        self.soapyConfig = soapyConfig
        self.range = self.soapyConfig.telCon.range
        self.slewRateConstant = self.soapyConfig.telCon.slewRate+0.0
        # print("telescopeSimpleController INIT COMPLETE")

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
    
    def calcSlewRate(self,error):
        self.slewRate = self.inRange(error)*self.slewRateConstant
        return self.slewRate




class telescopePidController(telescopeController):


    def __init__(self, soapyConfig):

        super().__init__(soapyConfig)
        self.Kp = self.soapyConfig.telCon.Kp
        self.Ki = self.soapyConfig.telCon.Ki
        self.Kd = self.soapyConfig.telCon.Kd

        # Calculated attributes
        self.P = (0.0,0.0)
        self.I = (0.0,0.0)
        self.D = (0.0,0.0)

        self.integral =  np.array((0.0,0.0))
    

    def calcSlewRate(self, error: np.ndarray):
        
        self.P = self.Kp*error
        
        self.integral += error
        self.I = self.Ki*self.integral
        
        self.D = self.Kd*(error - self.error)
        
        self.error = error
        self.slewRate = self.P + self.I + self.D
        return self.slewRate
    
class telescopeLeakyIntegratorController(telescopeController):
    def __init__(self, soapyConfig):
        super().__init__(soapyConfig)
        self.k1 = self.soapyConfig.telCon.k1
        self.k2 = self.soapyConfig.telCon.k2
        # Check in kl in range
        if self.k1 > 1 or self.k1 < 0:
            raise ValueError("k1 must be between 0 and 1")

        # Integral Term
        self.integral = np.array((0.0,0.0))

    def calcSlewRate(self, error):
        self.integral = (1-self.k1)*(self.integral + error)
        P = self.k2*error
        self.slewRate = (P + self.integral)
        return self.slewRate