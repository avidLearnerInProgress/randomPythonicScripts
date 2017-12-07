from pygeocoder import Geocoder
import numpy as np
import sys

def get_distance(source,destination):
    #used haversine forumla .. Couldn't understand the math behind Haversine :(
    radius=6371.0
    dlat=np.deg2rad(destination[0]-source[0])
    dlon=np.deg2rad(destination[1]-source[1])
    a=np.sin(dlat/2)*np.sin(dlat/2)+\
        np.cos(np.deg2rad(source[0]))*np.cos(np.deg2rad(destination[0]))*\
        np.sin(dlon/2)*np.sin(dlon/2) 
    c=2*np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return radius*c 

def get_latitudelongitude(location):
    return Geocoder.geocode(location)[0].coordinates
        
def convert_km_to_miles(km):
    miles_per_km=0.621371192
    return km*miles_per_km

def get_units_input():
    units=''
    while units!='m' and units!='km':
        userIp=int(input("Choose unit of distance.\n Press 1 for Mile\n Press 2 for Kilometer\n"))
        if userIp==1:
            units='m'
        elif userIp==2:
            units='km'
        else:
            print('Improper Input. Try again: ')
    return units
    
def main():
    sourceCity=str(input("Enter Source: "))
    destinationCity=str(input("Enter Destination: "))
    units=get_units_input()
    try:
        distance=get_distance(get_latitudelongitude(sourceCity),get_latitudelongitude(destinationCity))
        print("Distance between "+sourceCity+" and "+destinationCity+" is: ",end='')
        if units=='km':
            print(str(distance),'km')   
        else:
            distance=convert_km_to_miles(distance)
            print(str(distance),'miles') 
    except:
        print('Error, check your inputs!')
             
if __name__ == '__main__':
    sys.exit(main())