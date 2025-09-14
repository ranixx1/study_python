import requests

API_KEY = "e60366b6ffff15f1283dbe68ee0c505e"
cidade = "São Paulo do Potengi"

params = {
    "q": cidade,
    "appid": API_KEY,
    "units": "metric",
    "lang": "pt_br"
}

response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Clima em {data['name']}, {data['sys']['country']}:")
    print(f"Temperatura: {data['main']['temp']}°C")
    print(f"Descrição: {data['weather'][0]['description']}")
    print(f"Umidade: {data['main']['humidity']}%")
    print(f"Vento: {data['wind']['speed']} m/s")
else:
    print("Erro na requisição:", response.status_code, response.text)
