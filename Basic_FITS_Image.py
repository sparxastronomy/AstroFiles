import matplotlib.pyplot as plt
from astropy.io import fits
import astropy.visualization as viz

image_name=input("Please enter the name of the file : ")
hdul=fits.open(image_name)
hdul.info()
header_number=int(input("Enter Header number whose data  you want view : "))
image=hdul[header_number].data
hdul.close()
##stretching and normalizing using LogStretch() and MinMaxInterval() like in DS9
log_param=float(input("Enter base value for logrithmic stretch : "))
norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch())
plt.imshow(image,cmap='gray',norm=norm)
plt.show()
