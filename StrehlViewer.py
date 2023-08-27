'''
Plot Commands sent to DM
'''
import aotools
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import astropy.io.fits as fits
import os
# check if path is handed to script as argument
import sys
if len(sys.argv) > 1:
    file_path = sys.argv[1]
# Open a dialogue box to select the .fits file
#     root = tk.Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename()

#Open a dialogue box to select the directory
else:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()


# Check file_path is not empty
if file_path == "":
    raise ValueError("No file selected")

# Check in file path for instStrehl.fits and longStrehl.fits
instStrehlPath = file_path + "/instStrehl.fits"
longStrehlPath = file_path + "/longStrehl.fits"
if os.path.exists(instStrehlPath):
    file_path = instStrehlPath
    image = fits.getdata(file_path)
    plt.plot(image[0], label="Inst Strehl") 
if os.path.exists(longStrehlPath):
    file_path = longStrehlPath
    image = fits.getdata(file_path)
    plt.plot(image[0], label="Long Strehl") 

plt.legend()
plt.show()