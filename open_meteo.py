#Consultar os dados meteorológicos
import requests
import dotenv
import os

url = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&current=temperature_2m,relative_humidity_2m,wind_speed_10m,apparent_temperature,precipitation"

resposta = requests.get(
    url, params = {
	"latitude": 52.52,
	"longitude": 13.41,
    "timezone" : "GMT",
	"current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "precipitation", "wind_speed_10m"]
},
    timeout=15
)

resposta.raise_for_status()

if resposta == 200:
    print("Está tudo certo!")
else:
    print("Não está certo")

#current está dando erro
dados = resposta.json()
umidade = dados["current"]["relative_humidity_2m"]



