from datetime import datetime
from datetime import date
current_date = date.today()
current_time = datetime.now().time()

day_of_week = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье" }
month = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"}

def time():
    message = "Сегодня " + day_of_week[current_date.weekday()] + ", " + str(current_date.day) + " " + str(month[current_date.month]) + " " + str(current_date.year) + "г.\nВремя " + str(current_time.hour).zfill(2) + ":" + str(current_time.minute).zfill(2) + " по Минску"
    return message