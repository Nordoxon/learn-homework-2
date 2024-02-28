"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    dt_yes = datetime.now() - timedelta(1)
    dt_30 = datetime.now() - timedelta(30)
    print(f"Сегодня: {dt_now}")
    print(f"Вчера: {dt_yes}")
    print(f"30 дней назад: {dt_30}")

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print() #просто пустая строка для разделения
    print(str_2_datetime("01/01/20 12:10:03.234567"))
