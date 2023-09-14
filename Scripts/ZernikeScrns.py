'''
Build a static phase scrn using Zernike polynomials
'''
import aotools
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import astropy.io.fits as fits

# Dialogue Box to ask if we should save
def yes_no_dialog():
    response = messagebox.askyesno("Save?", "Do you want to continue?")
    return response

def save_as_fits():
    # Open a dialogue box to get the path
    path = filedialog.asksaveasfilename()
    if path:
        fits.writeto(path, scrn, overwrite=True)

if __name__ == "__main__":
    zernikeCoeffs = [0,10,-10]
    N = 130

    zernikeModes = aotools.zernike.zernikeArray(3,N)
    scrn = np.zeros((N,N))
    for i, Z in enumerate(zernikeModes):
        scrn += Z*zernikeCoeffs[i]

    plt.imshow(scrn)
    plt.colorbar()
    plt.show()

    if yes_no_dialog():
        save_as_fits()