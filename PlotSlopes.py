'''
Grab slopes.fits file and plot it
'''
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt
# Grab the slopes.fits file
path_static  = "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/OCGS_SMF/2023-08-28-12-05-21/slopes.fits"
path_TTError = "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/OCGS_SMF/2023-08-28-12-02-18/slopes.fits"
# Open the file
slopes = fits.getdata(path_TTError)

Tips = slopes[:,0]
Tilts = slopes[:,1]

# Create Subplot with 2 rows and 2 columns
fig, ax = plt.subplots(2,2)
ax[0,0].plot(Tips,label="Tip")
ax[0,0].plot(Tilts,label="Tilt")
ax[0,0].legend()
ax[0,0].set_title("Slopes")

# Convert Tips and Tilts to angles and radii
Radii = np.sqrt(Tips**2 + Tilts**2)
Angles = np.arctan2(Tilts,Tips)
ax[1,0].plot(Radii,label="Radius")
ax[1,1].plot(Angles,label="Angle")
ax[1,0].legend()
ax[1,1].legend()
ax[1,0].set_title("Radius")
ax[1,1].set_title("Angle")

# Extract frequencies from radii
freqs = np.fft.fftfreq(len(Radii))
# Plot Frequency Spectrum
ax[0,1].plot(freqs,np.fft.fft(Radii))
ax[0,1].set_title("Frequency Spectrum")

plt.show()