import os, telebot, time
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone
from telebot import types

DATE = datetime.now(timezone('Europe/Moscow'))


# LOAD .env FILE
def get_token():
    for file in os.listdir(".\config"):
        if file.endswith(".env"):
            dotenv_path = os.path.join(os.path.dirname(__file__) + "\config", file)
    try:
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            secret = os.getenv('SECRET')
            return secret
    except UnboundLocalError:
        print(f"Can't find your *.env file in directory {os.path.dirname(__file__) + '/config'}")
        time.sleep(0.001)
        exit()


def main():
    bot = telebot.TeleBot(get_token())
    print("Бот запущен")
    bot.send_message(chat_id=1002608184, text=f"Бот запущен в {DATE.hour}"
                                              f":{DATE.minute}"
                                              f" по МСК"
                                              f", {DATE.day}"
                                              f".{DATE.month}"
                                              f".{DATE.year}")

    # ВЫВОД СООБЩЕНИЯ ПРИ КОМАНДЕ START
    @bot.message_handler(commands='start')
    def start_message(start_msg):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        slave_button = types.KeyboardButton(text="Узнать имя работяги")
        keyboard.add(slave_button)
        next_slave_button = types.KeyboardButton(text="Кто же следующий")
        keyboard.add(next_slave_button)
        help_button = types.KeyboardButton(text="/help")
        keyboard.add(help_button)
        bot.send_message(start_msg.chat.id, "Для получения списка комманд введи /help", reply_markup=keyboard)

    # ПРОСЛУШКА ЧАТА И РЕАКЦИИ
    @bot.message_handler(content_types=['text'])
    def get_text_message(message):
        if message.text == "Привет" or message.text == "/start":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "/worker - Узнать, кто сегодня дежурит\n"
                                                   "/nextworker - Узнать, кто дежурит следующим")
        elif message.text == "/worker" or message.text == "Узнать имя работяги":
            bot.send_message(message.from_user.id, "Worker WIP")
            #TODO func worker
        elif message.text == "/nextworker" or message.text == "Кто же следующий":
            bot.send_message(message.from_user.id, "NextWorker WIP")
            #TODO func nextworker
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help или используй кнопку")

    bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    main()