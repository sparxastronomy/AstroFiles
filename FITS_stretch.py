import matplotlib.pyplot as plt
from astropy.io import fits
import astropy.visualization as viz

#logrithmic stretch and normalization
def log_try_and_except(image_name):
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
            plt.subplot(1,2,1)
            norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch(log_param))
            plt.imshow(image,cmap='gray',norm=norm)
            plt.title('a='+str(log_param))
            plt.grid(True)
            plt.subplot(1,2,2)
            log_param=previous_parameter
            norm=viz.ImageNormalize(image,interval=viz.MinMaxInterval(),stretch=viz.LogStretch(log_param))
            plt.imshow(image,cmap='gray',norm=norm)
            plt.title('a='+str(previous_parameter))
            plt.grid(True)
        else:
            plt.imshow(image,cmap='gray',norm=norm)
        plt.show()
        ch=input("Are you happy with your choice of log_parameters(Y/N) : ")
        if ch=='Y' or ch=='y':
            return norm(image)
            print("Image returned")
            flag=0
        else:
            flag=1 
            total_count+=1
            previous_parameter=log_param 

def log(file_name):
 try:
     log_try_and_except(file_name)
 except(TypeError):
     print("INCORRECT header chosen for viewing the data !!!! ")
     print("Please enter correct header number!!!\n")
 except(IndexError):
     print("HEADER UNIT not found!!!\nPlease recheck!!!\n")
     log_try_and_except(file_name)
