import telebot
from Bot import Bot

token = ''

bot = telebot.TeleBot(token)
botHelper = Bot(bot)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет/Здравствуй/добрый день - команды для приветствия.\n"
                          "Дела/Что нового/Как ты - команды для моего состояния\n"
                          "Погода/Завтра - команды для погоды на завтра\n"
                          "Анекдот/Шутка/Гоблин - команды для шутки")

@bot.message_handler(content_types=['document', 'audio', 'photo', 'audio', 'video', 'sticker'])
def handle_media(message):
    botHelper.handle_media(message)

@bot.message_handler(content_types=['text'])
def handle_media(message):
    botHelper.handle_text(message)

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()
