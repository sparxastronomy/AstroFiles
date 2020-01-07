import FITS_stretch as stretch
import RGB as RGB

print("        ~~ Available options ~~ \n")
print("     1.View Image and Stretch ")
print("     2.Plot an RGB image  ")
choice=int(input("\n\n  ENTER CHOICE : "))
if choice==1:
    file_name=input("Please Enter file name : \n")
    print("~~~~~~~~~~AVAIABLE STRETCH~~~~~~~~~~\n")
    print("\t1.LogStretch(default a=1000)")

    #input of stretch choice
    st_ch=int(input("\n\nEnter the number whose stretch you want to apply : "))
    if st_ch==1:
        stretch.log(file_name)
if choice==2:
    RGB.RGB_with_same_stretch()
