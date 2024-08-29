import requests

def get_news(country,fromdate,todate,apikey="b79a448b4a60479283c7dae98f83c3d7"):
    r = requests.get(f"https://newsapi.org/v2/everything?qInTitle={country}&from={fromdate}&to={todate}&sortBy=popularity&language=en&apiKey={apikey}")
    content = r.json()
    # print(content['articles'])

    for article in content['articles'][:5]:
        print(article['title'])


def get_weather(city,apikey='2cac8f580da8bd6dce0628125dfda27f'):
    content = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&limit=1&appid={apikey}").json()
    with open('weather_data.text','a') as file:
        for dicty in content['list']:
            file.write(f"{city},{dicty['dt']},{dicty['main']['temp']},{dicty['weather'][0]['main']}\n")

# get_news('india','2024-08-27','2024-08-28')
get_weather('Kolkata')
