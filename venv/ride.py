import uber_rides
import googlemaps
import json

gm=googlemaps.Client(key='AIzaSyB5GBK4ZHMqsmvSV6yWwE9gUw-T26MXnlM')
geocode_result=gm.geocode('Doraha,Ludhiana,Punjab,India')
#print(json.dumps(geocode_result,indent=4))
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']
print(lat,lng)