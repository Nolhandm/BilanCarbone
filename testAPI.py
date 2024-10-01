import requests
import pandas as pd
import matplotlib.pyplot as plt

params = {"km" : "6"}
response = requests.get("https://impactco2.fr/api/v1/transport", params=params)
#response = requests.get("https://data.ademe.fr/data-fair/api/v1/datasets/base-carboner/lines", params=params)
print(response.text)

datas = pd.read_excel('Datas.ods',[0,1])
print(datas[0])
#print(datas["Distance"])

fig, ax = plt.subplots()
#ax.plot(datas["Mode de transport"],datas["Distance"])
plt.show()