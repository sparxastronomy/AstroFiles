# ASTRO FILES
This project is an attempt to create scripts to process multiwavelength data

#  Requirements 
>  * Python3.x 
>  * Matplotlib
>  * Numpy
>  * Astropy
>  * Astroquery(for testing MAST integration)
>  * CIAO for working with CXC eventfiles
> * [Astronconda](https://astroconda.readthedocs.io/en/latest/) environment for HST image alignement

# Usage Guidelines  
One can directly load [**image_operations**](./image_operations.py) to directly view all the functionality.     
Only logarithmic stretching is added and will add more in future.
Till now RGB image with same stretch is available.      
It can read **.fz** file extensions too as they are only compressed fits files. 

**<del>CXC event files are still not compatible</del>**

## **Viewing CXC files using CIAO and Python**
1. Use *DS9* to view interested CXC event file(image)
2. Extract region of interets using DS9's 'region' function
3. Use the [**extract.sh**](./Chandra/extract.sh) script to convert the CXC event **(image)** file to python readable '.fits' file.
   * More information is provided in the script             
4. Important things to keep in mind:       
   * WCS information will be preserved
   * Spectral Information will be lost
   * Take special care if you '.reg' file is not one of the standrd regions ex. Annulus Region (lookout for region definition conflicts between DS9 and CIAO)
        * For such regions use this command before running the script to convert the region definition to CIAO format
        > convert_ds9_region_to_ciao_stack &nbsp; ds9.reg &nbsp; ciao.reg  

        *ds9.reg*   :  non-standard region        
        *ciao.reg*  :  Output .reg file in CIAO format

**MAST** integration is still in progress, if you want to try load [**mast_integration**](/mast_integration.py)   

For those who want to learn I've added Jupyter Notebook for [**basic fits viewing**](./Notebooks/FITS_file_viewing_and_stretching.ipynb).  
In future notebooks with advance functionality will be added too.

## Incoming Updates
* Updated streteching definition
* Jupyter Notebook for image HST image Alignment
* Jupyter Notebook for Multi-wavelength composition
* Useful CIAO scripts for spectral studies
