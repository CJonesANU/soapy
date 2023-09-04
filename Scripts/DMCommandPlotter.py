'''
Plot Commands sent to DM
'''
import aotools
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import astropy.io.fits as fits

# check if path is handed to script as argument
import sys
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
# Open a dialogue box to select the .fits file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

# Open the .fits file
image = fits.getdata(file_path)
# Handle error if file is not a .fits file
if image is None:
    raise ValueError("File is not a .fits file")

print(image.shape)
plt.plot(image[:,0], label="Tip")
plt.plot(image[:,1], label="Tilt")
plt.legend()
plt.show()