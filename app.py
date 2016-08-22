import urllib3, json


def get_data(cities):
	link = "http://api.openweathermap.org/data/2.5/weather?&units=metric&appid=2bc3e79bb974a007818864813f53fd35"
	http = urllib3.PoolManager()
	results = []
	for city in cities:
		url = link + "&q="+city
		result = http.request("GET", url)
		data = json.loads(result.data)
		results.append(data)
	return results
		

cities = ["Nairobi", "Kampala", "Lagos", "London", "Amsterdam", "Djamema", "Bungoma"]
data = get_data(cities)
print "City".ljust(16), 
print "Temp".ljust(16), 
print "Description".ljust(16),
print "Country".ljust(16)
print("="*60)

for x in data:
	print x['name'].ljust(16),
	print str(x['main']['temp']).ljust(16),
	print (x['weather'][0]['description']).ljust(16),
	print (x['sys']['country']).ljust(16)

	