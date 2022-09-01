import random
import BotEnums
import requests
from bs4 import BeautifulSoup

class Bot:
    def __init__(self, bot):
        self.bot = bot

    def handle_text(self, message):
        message_text = message.text
        message_text = message_text.lower().split()
        hello_trigger = False
        feeling_trigger = False
        weather_trigger = False
        joke_trigger = False
        for word in message_text:
            for string in BotEnums.hello_requests:
                if word == string:
                    hello_trigger = True
            for string in BotEnums.feeling_requests:
                if word == string:
                    feeling_trigger = True
            for string in BotEnums.weather_requests:
                if word == string:
                    weather_trigger = True
            for string in BotEnums.joke_request:
                if word == string:
                    joke_trigger = True
        if hello_trigger:
            self.bot.send_message(message.chat.id,
                                  BotEnums.hello_phrases[random.randint(0, len(BotEnums.hello_phrases) - 1)])
        if feeling_trigger:
            self.bot.send_message(message.chat.id,
                                  BotEnums.feeling_responses[random.randint(0, len(BotEnums.feeling_responses) - 1)])
        if weather_trigger:
            self.bot.send_message(message.chat.id, self.get_weather())
        if joke_trigger:
            self.bot.send_message(message.chat.id, self.get_joke())
        if not hello_trigger and not feeling_trigger and not weather_trigger and not joke_trigger:
            self.bot.send_message(message.chat.id, "Не понимаю тебя...")

    def get_weather(self):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'id': "524901", 'units': 'metric', 'lang': 'ru', 'APPID': BotEnums.weather_api_key})
            data = res.json()
            return "Прогноз на завтра:\n" + 'Температура: {0:+3.0f}\n'.format(data['list'][0]['main']['temp'])\
                   + "Описание погоды: " + data['list'][0]['weather'][0]['description']
        except Exception as e:
            return "Не могу получить погоду потому что " + str(e)

    # Funny function requested by mentor
    # Trying to get "Goblins" best moments from 2ach thread
    # This sometimes is causing 404, and videos that are cannot be played
    def get_joke(self):
        try:
            res = requests.get("https://2ch.hk/b/arch/2020-04-02/res/216775069.html")
            soup = BeautifulSoup(res.text, "lxml")
            media = soup.findAll('a',{'class':'post__image-link'})
            #media = soup.find_all("a", class_="post__image-link")
            videos = []
            for video in media:
                if '.mp4' in video.get('href'):
                    videos.append("https://2ch.hk/" + video.get('href'))


            # while True:
            #     video_link = videos[random.randint(0, len(videos) - 1)]
            #     res = requests.get(video_link)
            #     print(res)
            #     if res.status_code != 404:
            return "Посмотри видео анекдот от гоблина:\n\n" + videos[random.randint(0, len(videos) - 1)]
        except Exception as e:
            return "Не могу получить погоду потому что " + str(e)

    def handle_media(self, message):
        self.bot.send_sticker(message.chat.id, BotEnums.stickers[random.randint(0, len(BotEnums.stickers) - 1)])