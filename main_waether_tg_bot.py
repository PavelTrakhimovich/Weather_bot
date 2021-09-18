import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Короче пиши сюда название города типа Minsk и я пришлю тебе сводку погоды.")

@dp.message_handler()
async def get_weather(message:  types.Message):
    try:
        r = requests.get (
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
    

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d- %H:%M')}***\n"
                 f"Погода в городе {city}\nТемпература: {cur_weather}С°\n"
                 f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\n"
                 f"Скорость ветра:{wind_speed} м/с\nВосход солнца: {sunrise_timestamp}\n"
                 f"Закат солнца: {sunset_timestamp}\nДлительность дня {length_of_the_day}"
                )

    except:
        await message.reply ("Проверьте название города")


if __name__ == "__main__":
    executor.start_polling(dp)
