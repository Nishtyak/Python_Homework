# Задача 34:
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает,
# Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def check_letters(words):
    check_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for el in check_list:
            count += words.count(el)
    return count

poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
poem_words = poem.split()

if len(set(list(map(check_letters, poem_words)))) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')


