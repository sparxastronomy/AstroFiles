import matplotlib.pyplot as plt
from astropy.io import fits
import astropy.visualization as viz

def image_viewing_with_header(image_name,header_number):
    hdul=fits.open(image_name)
    image=hdul[header_number].data
    hdul.close()
    ##stretching and normalizing using LogStretch() and MinMaxInterval() like in DS9
    log_param=float(input("Enter base value for logrithmic stretch : "))
    norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch(log_param))
    plt.imshow(image,cmap='gray',norm=norm)
    plt.show()

def image_viewing(image_name):
    hdul=fits.open(image_name)
    hdul.info()
    header_number=int(input("Enter Header number whose data  you want view : "))
    image=hdul[header_number].data
    hdul.close()
    ##stretching and normalizing using LogStretch() and MinMaxInterval() like in DS9
    log_param=float(input("Enter base value for logrithmic stretch : "))
    norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch(log_param))
    plt.imshow(image,cmap='gray',norm=norm)
    plt.show()

#choice of function:
view_ch=int(input(" Do you want to view image with supplied header(1) or you want to view available headers and then analyze(2) : "))
if view_ch==1:
    image_name   =input("Please enter the name of the file : ")
    header_number=input("Please input header nnumber : ")   
    image_viewing_with_header(image_naem,header_number)
else:
    image_name=input("Please enter the name of the file : ")
    image_viewing(image_name)