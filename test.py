from sunlight import openstates
from googlegeocoder import GoogleGeocoder

geocoder = GoogleGeocoder()

address = raw_input("please enter your address: ")

search = geocoder.get(address)

latitude = search[0].geometry.location.lat
longitude = search[0].geometry.location.lng

location = openstates.legislator_geo_search(latitude, longitude)

for legislators in location:
	print "%s %s" % (legislators['full_name'], legislators['photo_url'])
