import requests

params = {"km" : "6"}
response = requests.get("https://impactco2.fr/api/v1/transport", params=params)
print(response.text)