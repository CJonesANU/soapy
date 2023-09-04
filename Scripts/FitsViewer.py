'''
Helper script in python to view .fits files

When running the script, a dialogue box opens to select the path to the .fits file
It is then opened by the aotools library and displayed by matplotlib.pyplot
'''
import aotools
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, filedialog
import astropy.io.fits as fits


def open_file_dialog():
    file_path = filedialog.askopenfilename()

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


# Display the image
plt.imshow(image)
plt.colorbar()
plt.show()