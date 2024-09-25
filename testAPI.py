import requests
import pandas as pd
import matplotlib.pyplot as plt

params = {"km" : "6"}
response = requests.get("https://impactco2.fr/api/v1/transport", params=params)
#print(response.text)

datas = pd.read_excel('Datas.ods')
print(datas)
print(datas["Distance"])

fig, ax = plt.subplots()
ax.plot(datas["Mode de transport"],datas["Distance"])
plt.show()