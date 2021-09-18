from os import P_PGID
import datetime
import requests
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get (
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d- %H:%M')}***\n"
                 f"Погода в городе {city}\nТемпература: {cur_weather}\n"
                 f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\n"
                 f"Скорость ветра:{wind_speed}\nВосход солнца: {sunrise_timestamp}\n"
                 f"Закат солнца: {sunset_timestamp}\nДлительность дня {length_of_the_day}/n"
                 "Хорошего Дня!))"
                )
    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
