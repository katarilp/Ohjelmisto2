import requests
import json

pyyntö = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyyntö).json()

#print(vastaus)
#print(json.dumps(vastaus, indent=2))

print(vastaus["value"])