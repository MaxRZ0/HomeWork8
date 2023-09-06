#  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе

import os

# lst1 = [['Иван', 'Иванов'], ['Петр', 'Петров']]

def menu():
    phone_book = list()
    while True:
        print('Введите 1 для создания новвой записи')
        print('Введите 2 для изменеия записи')
        print('Введите 3 для поиска записи')
        print('Введите 4 для удаления записи')
        print('Введите 5 для вывода телефонного справочника')
        print('Введите 6 для экспорта данных из файла')
        print('Введите 7 для импорта данных в файл')
        print('Введите 8 для выхода из справочника')
        choise = int(input('Ваш выбор: '))
        if choise == 8:
            print('Вы выбрали выход')
            return
        if choise == 1:
            print('Вы выбрали 1, добавить данные')
            phone_book = create_record(phone_book, get_user_data())
        if choise == 5:
            print('Вы выбрали 5, вывести ТС')
            print_phone_book(phone_book)
        if choise == 6:
            print('Вы выбрали 6, экспорт данных из файла')
            create_from_data(phone_book, get_file_name(), ',')
        if choise == 3:
            print('Вы выбрали 3, найти запись')
            read_from_data(phone_book, data_for_read())
        if choise == 2:
            print('Вы выбрали 2, изменить запись')
            phone_book = update_phone_book(phone_book, data_for_read(),get_user_data())
        if choise == 4:
            print('Вы выбрали 4, удалить запись')
            phone_book = del_record(phone_book, data_for_read())
        if choise == 7:
            print('Вы выбрали 7, импорт данных в файл')
            export_data(phone_book, get_file_name())

def get_user_data() -> list:
    name = input('Введите имя: ')
    sur_name = input('Введите фамилию: ')
    phone_num = input('Введите номер телефона: ')
    desc = input('Введите описание: ')
    return [name,sur_name,phone_num,desc]

def create_record(gb_phone_book: list, user_data: list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book

def get_file_name() -> str:
    return input('Введите имя файла: ')

def create_from_data(gb_phone_book: list, file_name: str, delimiter:str) -> list:
    path_data = os.path.join('.', file_name)
    with open(path_data, 'r', encoding='utf-8') as data:
        for line in data:
            gb_phone_book = create_record(gb_phone_book, line.strip().split(delimiter))
    return gb_phone_book

def print_phone_book(gb_phone_book:list) -> None:
    for idx in gb_phone_book:
        print(idx)

def data_for_read() -> str:
    return input('Введите фамилию нужного человека: ').capitalize()

def read_from_data(gb_phone_book: list, readed_data: str) -> None:
    for line in gb_phone_book:
        for idx in range(len(line)):
            if readed_data == line[idx]:
                print(line)

def update_phone_book(gb_phone_book: list, readed_data: list, user_data: list) -> list:
    for line in gb_phone_book:
        for idx in range(len(line)):
            if readed_data == line[idx]:
                line[:] = user_data
    return gb_phone_book

def del_record(gb_phone_book: list, readed_data: list) -> list:
    for line in gb_phone_book:
        for idx in range(len(line)):
            if readed_data == line[idx]:
                line.clear()
                return gb_phone_book
    return gb_phone_book

def export_data(gb_phone_book: list, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as exp_data:
        for line in gb_phone_book:
            for idx in range(len(line)):
                exp_data.writelines(line[idx])
                if idx == (len(line)-1):
                    exp_data.writelines('\n')
                else:
                    exp_data.writelines(', ')

menu()
