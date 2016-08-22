import urllib3, json
http = urllib3.PoolManager()
link = "http://api.openweathermap.org/data/2.5/weather?&units=metric&appid=2bc3e79bb974a007818864813f53fd35"
cities=["Nairobi", "Kampala", "Lagos", "London", "Amsterdam"]
print "City".ljust(16), 
print "Temp".ljust(16), 
print "Description".ljust(16),
print "Country".ljust(16)
print("="*60)

def get_data(cities):
	for city in cities:
		url = link + "&q="+city
		result = http.request("GET", url)
		data = json.loads(result.data)
		print data['name'].ljust(16),
		print str(data['main']['temp']).ljust(16),
		print str(data['weather'][0]['description']).ljust(16),
		print str(data['sys']['country']).ljust(16)

get_data(cities)
	