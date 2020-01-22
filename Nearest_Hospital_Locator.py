# Python program to get a set of 
# places according to your search 
# query using Google Places API 

# importing required modules 
import requests, json 
import googlemaps
import pprint
import time
import Get_Api
# enter your api key here 
API_KEY=Get_Api.function()
gmaps=googlemaps.Client(key=API_KEY)

# url variable store url 
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search 
query = 'hospital' 

# get method of requests module 
# return response object 
r = requests.get(url + 'query=' + query +
						'&key=' + API_KEY) 

# json method of response object convert 
# json format data into python format data 
places_result = r.json() 

# now x contains list of nested dictionaries 
# we know dictionary contain key value pair 
# store the value of result key in variable y 

for place in places_result['results']:

	my_place_id=place['place_id']

	my_fields=['name','formatted_phone_number']

	place_details=gmaps.place(place_id=my_place_id,fields=my_fields)

	pprint.pprint(place_details['result']['name']+':'+place_details['result']['formatted_phone_number'])

	