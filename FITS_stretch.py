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
    total_count=1
    previous_parameter=0
    while(flag!= 0):
        ##stretching and normalizing using LogStretch() and MinMaxInterval() like in DS9
        log_param=float(input("Enter base value for logrithmic stretch : "))
        norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch(log_param))
        if total_count>1:
            fig,(ax1,ax2) = plt.subplots(1, 2)
            norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch(log_param))
            ax1.imshow(image,cmap='gray',norm=norm)
            ax1.title.set_text('a='+str(log_param))
            log_param=previous_parameter
            norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch(log_param))
            ax2.imshow(image,cmap='gray',norm=norm)
            ax2.title.set_text('a='+str(previous_parameter))
        else:
            plt.imshow(image,cmap='gray',norm=norm)
        plt.show()
        ch=input("Are you happy with your choice of log_parameters(Y/N) : ")
        if ch=='Y' or ch=='y':
            flag=0
            return norm(image)
        else:
            flag=1 
            total_count+=1
            previous_parameter=log_param  
