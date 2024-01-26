import requests

API_KEY = "4e98cc93ffa2687dc7a034b1cb623e89"

url = "http://api.openweathermap.org/data/2.5/weather?q=Nairobi&appid=4e98cc93ffa2687dc7a034b1cb623e89"

response = requests.get(url)

data = response.json()

print (data['coord'])
