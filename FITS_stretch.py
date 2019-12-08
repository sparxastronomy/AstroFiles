import matplotlib.pyplot as plt
from astropy.io import fits
import astropy.visualization as viz

#logrithmic stretch and normalization
def log(image_name):
    hdul=fits.open(image_name)
    hdul.info()
    header_number=int(input("Enter Header number whose data  you want view : "))
    image=hdul[header_number].data
    hdul.close()
    flag=1
    while(flag!= 0):
        ##stretching and normalizing using LogStretch() and MinMaxInterval() like in DS9
        log_param=float(input("Enter base value for logrithmic stretch : "))
        norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch(log_param))
        plt.imshow(image,cmap='gray',norm=norm)
        plt.show()
        ch=input("Are you happy with your choice of log_parameters(Y/N) : ")
        if ch=='Y':
            return norm(image)
            flag=0
        else:
            flag=1   
