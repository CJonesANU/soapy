'''
Analyse the spots of previously generated Sci Images form SOAPY Simulations
'''

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
import aotools
import astropy.io.fits as fits

# Define function to find the center of a spot in polar coordinates
def findCenter(image, method):
    if method == "COG":
        centre = aotools.centroiders.centre_of_gravity(image)
    if method == "BP":
        centre = aotools.centroiders.brightest_pixel(image,0.5)
    nx,ny = image.shape
    centreRel = (centre[0] - nx/2, centre[1] - ny/2)
    radius = np.sqrt(centreRel[0]**2 + centreRel[1]**2)
    angle = np.arctan2(centreRel[1], centreRel[0])
    return radius, angle
    

# Grab Image that was not TT Affected
# Open the .fits file
path = "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/OCGS_SMF/2023-08-25-10-56-24/sciPsf_00.fits"
unaffectedImage = fits.getdata(path)
# Grab Image that was TT Affected
path =  "/home/cameron/Documents/projects/SOAPY_TTError/soapy-1/OCGS_SMF/2023-08-25-10-56-00/sciPsf_00.fits"
affectedImage = fits.getdata(path)

# Plot them both using imshow
fig, ax = plt.subplots(1,2)
ax[0].imshow(unaffectedImage)
ax[0].set_title("Unaffected Image")
ax[1].imshow(affectedImage)
ax[1].set_title("Affected Image")
# Plot without blocking
plt.show(block=False)

# Find the center of the spot in polar coordinates for both images
radiusCOG_u, angleCOG_u = findCenter(unaffectedImage, "COG")
radiusBP_u, angleBP_u = findCenter(unaffectedImage, "BP")

# Report Results for both methods to 2 decimal places

radiusCOG_a, angleCOG_a = findCenter(affectedImage, "COG")
radiusBP_a, angleBP_a = findCenter(affectedImage, "BP")

# Get Strehl Ratios of both images
srUnaffected = np.max(np.abs(unaffectedImage))**2 / np.sum(np.abs(unaffectedImage)**2)
srAffected = np.max(np.abs(affectedImage))**2 / np.sum(np.abs(affectedImage)**2)


# Get the azimuthal average of each image and plot them on a new single figure

unaffectedAziAvg = aotools.image_processing.azimuthal_average(unaffectedImage)
affectedAziAvg   = aotools.image_processing.azimuthal_average(affectedImage)  

fig, ax = plt.subplots(1,1)
ax.plot(unaffectedAziAvg, label="Unaffected")
ax.plot(affectedAziAvg, label="Affected")
ax.set_title("Azimuthal Average")
ax.set_xlabel("Radius")
ax.set_ylabel("Intensity")
ax.legend()
ax.set_xbound(0, 50)
plt.show(block=False)

# Use Azimuthal Average to find the FWHM of the spot
# Find the max of the unaffected image
maxUnaffected = np.max(unaffectedAziAvg)
# Find the index of the max
maxIndex = np.where(unaffectedAziAvg == maxUnaffected)[0][0]
# Find the first index where the value is less than half the max
halfMax = maxUnaffected / 2
# Find the index of the first value less than half the max
halfMaxIndex = np.where(unaffectedAziAvg < halfMax)[0][0]
# Find the difference between the two
fwhm_Unaffected = maxIndex - halfMaxIndex
encircledEnergy_unaffected = aotools.image_processing.psf.encircled_energy(unaffectedImage)

# Find the max of the affected image
maxAffected = np.max(affectedAziAvg)
# Find the index of the max
maxIndex = np.where(affectedAziAvg == maxAffected)[0][0]
# Find the first index where the value is less than half the max
halfMax = maxAffected / 2
# Find the index of the first value less than half the max
halfMaxIndex = np.where(affectedAziAvg < halfMax)[0][0]
# Find the difference between the two
fwhm_Affected = maxIndex - halfMaxIndex

encircledEnergy_affected = aotools.image_processing.psf.encircled_energy(affectedImage)


print("Unaffected Image")
print("----------------")
print("COG: Radius = {:.3f}, Angle = {:.3f}".format(radiusCOG_u, angleCOG_u))
print("BP:  Radius = {:.3f}, Angle = {:.3f}".format(radiusBP_u, angleBP_u))
print("----------------")

print("Affected Image")
print("----------------")
print("COG: Radius = {:.3f}, Angle = {:.3f}".format(radiusCOG_a, angleCOG_a))
print("BP:  Radius = {:.3f}, Angle = {:.3f}".format(radiusBP_a, angleBP_a))
print("----------------")

print("Strehl Ratio")
print("----------------")
print("Unaffected: {:.3f}".format(srUnaffected))
print("Affected:   {:.3f}".format(srAffected))
print("----------------")
print("FWHM")
print("Unaffected FWHM: {:.3f}".format(fwhm_Unaffected))
print("Encircled Energy: " + str(encircledEnergy_unaffected))

print("Affected FWHM: {:.3f}".format(fwhm_Affected))
print("Encircled Energy: " + str(encircledEnergy_affected))


# Block until user closes the plot
plt.show(block=True)
