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
    if query_choice==1:
        search_region=input(" Enter search region : ")
    else:
        search_target=input(" Enter search target : ")
    search_radius=input(" Enter search radius : ")
    
    mission_ID=input(" Enter mission specific constraint\n"+str(Observations.list_missions())+"\n otherwise leave empty : ")
        
    if query_choice==1:
        ObsByCriteria = Observations.query_criteria(obs_collection=mission_ID , object_region=search_region , radius=search_radius)
    else:
        ObsByCriteria = Observations.query_criteria(obs_collection=mission_ID , objectname=search_target , radius=search_radius)
    
    #query output
    
    print("Number of results:",len(ObsByCriteria))
    print(ObsByCriteria[:15])

    #dataproduct query
    print("\n~~~~ Viewing dataproducts query ~~~~")
    obsids = ObsByCriteria[0:2]['obsid']
    data_products_by_id = Observations.get_product_list(obsids)
    print(data_products_by_id)

    #filtering data products:
    productType=input("  Enter valid product type \n [SCIENCE, CALIBRATION, BIAS, DARK, FLAT, WAVECAL, NOISE, WEIGHT, AUXILIARY, INFO, CATALOG, LIGHTCURVE, TARGETPIXELS, PREVIEW, PREVIEW_FULL, PREVIEW_1D, PREVIEW_2D, THUMBNAIL, PREVIEW_THUMB, MINIMUM_SET, RECOMMENDED_SET, COMPLETE_SET, WEBSERVICE]\n     : ")
    Filtered_Products = Observations.filter_products(data_products_by_id,productType= productType,mrp_only=False)
    print(Filtered_Products)

search_and_list()
#advance serching and downloading