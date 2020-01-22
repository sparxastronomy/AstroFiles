# MAST
This project is an attempt to create scripts to process multiwavelength data and create an working AI to make data vizulaiztion easier though command line based interaction and speech synthesis.

#  Usage Guidance 
***Requirements:***
  * Python3.x 
  * Matplotlib
  * Numpy
  * Astopy
  * Astroquery(for testing MAST integration)
  
One can directly load [**image_operations**](./image_operations.py) to directly view all the functionality.
Only logarithmic stretching is added and will add more in future.
Till now RGB image with same stretch is available. Will add multiple strech options in future.
It can read **.fz** file extensions too as they are only compressed fits files. 
**CXC event files are still not compatible**
Image alignment is still not implemented as image alignment is quick and simple using PyRAF. 

**MAST** integration is still in progress, if you want to try load [mast_integration](/mast_integration.py) 

Till now no ML amd AI and no speech synthesis is used as basic scripting is not complete yet.
