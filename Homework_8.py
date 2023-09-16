# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной (наличие if и else)

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных и поиска по фамилии.

from os.path import exists
from csv import DictReader, DictWriter
import os

def get_info():
    info = []
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print("wrong number!")
            else:
                flag= True
        except ValueError:
            print("Неверно! Вы ввели буквы!")
    info.append(phone_number)
    return info

def create_file():
    with open("phone.csv", "w", encoding='utf-8') as data:
        # data.write('Фамилия;Имя;Номер телефона\n')
        f_n_writer = DictWriter(data, fieldnames =[ 'Имя', 'Фамилия', 'Номер'])
        f_n_writer.writeheader()

def write_file(lst):
    # with open("phone.txt", "a", encoding='utf-8') as data:
    #     data.write(f'{lst[0]};{lst[1]};{lst[2]}\n')
    with open('phone.csv', 'r+', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Имя', 'Фамилия', 'Номер'])
        for el in res:
            f_n_writer.writerow(el)

def read_file():
    # with open("phone.csv", encoding='utf-8') as data:
    #     phone_book = data.readlines()
    # return phone_book
    with open('phone.csv', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
        print(*phone_book[0].keys())
        for el in phone_book:
            print(*el.values())

def record_info():
    lst = get_info()
    write_file(lst)

def delete_entry(word):
    phone_book = []
    with open('phone.csv', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    create_file()
    with open('phone.csv', 'a', encoding='utf-8') as f_n:
        for el in phone_book:
            if el['Имя'] != word and el['Фамилия'] != word:
                f_n_writer = DictWriter(f_n, fieldnames=['Имя', 'Фамилия', 'Номер'])
                f_n_writer.writerow(el)

def change_entry(word, new_word):
    phone_book = []
    with open('phone.csv', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    create_file()
    with open('phone.csv', 'a', encoding='utf-8') as f_n:
        for el in phone_book:
            if el['Имя'] == word:
                el['Имя'] = new_word
            elif el['Фамилия'] == word:
                el['Фамилия'] = new_word
            f_n_writer = DictWriter(f_n, fieldnames=['Имя', 'Фамилия', 'Номер'])
            f_n_writer.writerow(el)

def search_entry(word):
    phone_book = []
    with open('phone.csv', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
        for el in phone_book:
            if el['Имя'] == word or el['Фамилия'] == word:
                print("Искомая запись: ")
                print(*el.values())


def main(): #выполняет функцию файлового ???
    while 1: #или while True
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан!')
                break
            read_file()
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 'd':
            if not exists('phone.csv'):
                print('Файл не создан!')
                break
            else:
                word = input("Введите имя или фамилию для удаления записи: ")
                delete_entry(word)
        elif command == 'c':
            if not exists('phone.csv'):
                print('Файл не создан!')
                break
            else:
                word = input("Введите имя или фамилию для изменения записи: ")
                new_word = input("Введите новое значение: ")
                change_entry(word, new_word)
        elif command == 's':
            if not exists('phone.csv'):
                print('Файл не создан!')
                break
            else:
                word = input("Введите имя или фамилию для поиска записи: ")
                search_entry(word)
main()