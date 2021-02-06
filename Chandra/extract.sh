punlearn dmcopy
dmcopy "file.fits[sky = region(extract.reg)][bin sky=1,energy=_:_]" file_temp.fits
dmcopy "file_temp.fits[bin sky=1]" file_extract.fits


#outline : Create a copy of the event file in interested energy range and then flatten the event file
#          so that it is python compatible

#about the commands
# dmcopy: copies a event file based on the parameters provided

#about the parameter
# sky = region(_)   : Works on ectracting area of sky you are interested in
# bin sky = 1       : Bins the sky to convert to a 2D image array (Binning event tables to an image)
# bin energy =_:_   : Extract energy information in given energy range(in eV)
#                     example, bin energy=700:1400 extracts data only in ergey range 0.7 -1.4 KeV

#about the files
# file.fits         : Event file you intend to work with
# extract.reg       : Region file containing information of about your Area of Interest
# file_temp.fits    : Temporary Event file containing energy only in interested region
# temp_extract.fits : Final extracted file Python compatible