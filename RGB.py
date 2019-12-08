import astropy.visualization as viz
import matplotlib.pyplot as plt
import FITS_stretch as stretch

red  = input("Enter name of the  red channel   : ")
green= input("Enter name of the  green channel : ")
blue = input("Ennter name of the blue channel  : " )

#function calling to view stretched image and save them 
print("~~~~~~~~~~AVAIABLE STRETCH~~~~~~~~~~")
print("\t1.LogStretch(default a=1000)")


#input of stretch choice
st_ch=int(input("Enter the number whose stretch you want to apply : "))
if st_ch==1:
    red=stretch.log(red)
    green=stretch.log(green)
    blue=stretch.log(blue)

#RGB image using lupton_RGB
RGB_image = make_lupton_rgb(red, green, blue, Q=10,stretch=0.5)
plt.imshow(RGB_image)
plt.show()