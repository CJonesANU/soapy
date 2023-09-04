import soapy
from soapy import confParse, atmosphere
import numpy as np
import matplotlib.pyplot as plt
import aotools
import os

nScreen = 1
r0 = 1
N = 130
pxl_scale = 0.00547
L0 = 10
l0 = 1

# CHeck if ./conf/scrn0.fits exists and delete it if it does
if os.path.exists('./conf/scrn0.fits'):
    os.remove('./conf/scrn0.fits')

PhaseScreens = atmosphere.makePhaseScreens(nScreen,r0,N,pxl_scale,L0,l0, DIR='./conf')

# Show the phase screens
plt.imshow(PhaseScreens[0])
plt.colorbar()
plt.show()
