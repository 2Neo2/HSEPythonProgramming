import requests, os, json
from dotenv import load_dotenv

load_dotenv()

URL_JSON = 'https://jsonplaceholder.typicode.com'
URL_WEATHER = 'https://api.openweathermap.org/data/2.5/weather'
URL_CITY = 'http://api.openweathermap.org/geo/1.0/direct'

# NOTE: Task_1.
def jsonplaceholder_request():
    url = f"{URL_JSON}/posts"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        posts = response.json()
        
        for post in posts[:5]:
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
            print("-" * 40)
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# jsonplaceholder_request()

# NOTE: Task_2.
def weather_info_request():
    city = input('Введите название города:').strip()
    url=f'{URL_CITY}?q={city}&limit=5&appid={os.environ["WEATHER_API_KEY"]}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        city_info = response.json()[0]

        lon = city_info['lon']
        lat = city_info['lat']
        url=f'{URL_WEATHER}?lat={lat}&lon={lon}&appid={os.environ["WEATHER_API_KEY"]}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_info = response.json()

            mess = (
                f"Weather: {weather_info['weather'][0]['main']}\n"
                f"Weather description: {weather_info['weather'][0]['description']}\n"
                f"Wind speed: {weather_info['wind']['speed']} m/s\n"
                f"Temp: {weather_info['main']['temp']} K\n"
                f"Feels like: {weather_info['main']['feels_like']} K\n"
                f"MAX: {weather_info['main']['temp_max']} K\n"
                f"MIN: {weather_info['main']['temp_min']} K"
            )
            print(mess)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении погоды: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении long latt для {city}: {e}")

weather_info_request()