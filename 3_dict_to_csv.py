"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    users = [
        {'name': 'Peter', 'age': '28', 'job': 'engineer', 'email': 'peter28@yahoo.com', 'car': 'Ford'},
        {'name': 'Alex', 'age': '51', 'job': 'doctor', 'email': 'alex51@gmail.com', 'car': 'Toyota'},
        {'name': 'John', 'age': '35', 'job': 'economist', 'email': 'JohnChampion@gmail.com', 'car': 'Chevrolet'},
        {'name': 'Sam', 'age': '40', 'job': 'writer', 'email': 'samknowyou@yahoo.com', 'car': 'Dodge'}
    ]


    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job', 'email', 'car']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in users:
            writer.writerow(user)
if __name__ == "__main__":
    main()
