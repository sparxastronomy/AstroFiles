#integration to MAST data base using astroquery.mast API

#imports
from astroquery.mast import Mast
from astroquery.mast import Observations
from astroquery.mast import Catalogs

#searching and listing
def search_and_list():
    print("     How do you want to search for object : ")
    print("         1. RA and DEC ")
    print("         2. Target Name Resolver ")
    query_choice=int(input(" Enter choice 1 or 2 : "))
    choice=False
    while(choice==False):
        if query_choice!=1 or query_choice!=2:
            re_query_choice=(" Invalid choice!!!! \n Do you want to continue entering correct option [y]/n :")
            if re_query_choice=='y' or re_query_choice=='Y':
                query_choice=int(input(" Enter correct choice 1/2 : "))
            else:
                SystemExit()
        choice=True
    #input through RA and DEC
    search_region=input(" Enter Query region : ")
    search_radius=input(" Enter search radius : ")
    print("Available missions : ", Observations.list_missions(),"\n")
    mission_ID=input(" Enter mission specific constraint"+Observations.list_missions()+" otherwise leave empty : ")
    dataproduct_type=input(" Enter Product type [IMAGE, SPECTRUM, SED, TIMESERIES, VISIBILITY, EVENTLIST, CUBE, CATALOG, ENGINEERING] otherwise leave empty : ")
    instrument_name=input(" Enter Instrument name[E.g. WFPC2/WFC, UVOT, STIS/CCD] otherwise leave empty : ")
    filters=input(" Enter filter name[E.g F469N, NUV, FUV] otherwise leave empty : ")
    max_wavelength=input(" Enter maximum wavelength(in nm) otherwise leave empty : ")
    min_wavelength=input(" Enter minimum wavelength(in nm) otherwise leave empty : ")
    proposal_ID=input(" Enter proposal ID otherwise leave empty : ")
    intentType=input(" Enter intent[science, calibration] otherwise leave empty : ")
    obs_ID=input(" Enter observation ID otherwise leave empty : ")
    calib_level=input("Enter callibration level( \n 0 = raw, 1 = uncalibrated, 2 = calibrated,\n 3 = science product, 4 = contributed science product) otherwise leave empty : ") 
    ObsBycriteria = Observations.query_criteria(obs_collection=mission_ID,objectname=search_region, radius=search_radius)
    print("Number of results:",len(ObsBycriteria))
    print(ObsBycriteria[:10])

search_and_list()
#advance serching and downloading