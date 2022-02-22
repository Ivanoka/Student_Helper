import os, telebot, time
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone

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

    @bot.message_handler(content_types=['text'])
    def get_text_message(message):
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши 'Привет'")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    main()