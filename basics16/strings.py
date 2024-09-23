"==================================Строки========================================="
# строки - неизменяемый, индексируемый, итерируемый тип данных, который предназначен для хранения текста, заключенного в одинарные или двойные кавычки

string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# error_string = 'неправильная строка"

string3 = "don't" # внутри двойных кавычек, все одинарные - просто символы
string4 = ' "ADA Courses" ' # внутри одинарных кавычек, все двойные - просто символы

string5 = '''
Многострочный текст
в одинарных кавычках
тут можно ставить "любые" 'кавычки'
'''

string6 = """
Многострочный текст
в одинарных кавычках
тут можно ставить "любые" 'кавычки'
"""

string7 = 'hello' + ' ' + 'world' # конкатенация строк (склеивание)
print(string7)

string_hello = 'hello'
string_world = 'world'
print(string_hello + ' ' + string_world) # тоже конкатенация

print(string_hello * 8) # hellohellohellohellohellohellohellohello

"=======================================Экранизация строк==============================="
# \n - перенос на новую строку
print('hello\nworld') # hello
#                       world

# \t - табуляция
print('hello\tworld') # hello   world

# \'  - отображение '
# \"  - отображение "

print('Don\'t')

"=================================Форматирование строк================================"
# product_title = input('Введите название товара: ')
price = 1000
# print('Название: product_title, цена: price') названия переменных внутри строки, не считаются переменными, они считаются просто символами
# print('Название:', product_title, 'цена: ', price)

# 1 способ (f-строки)
# format1 = f'Название: {product_title}\nЦена: {price}'
# print(format1)
"""
Название: Iphone 15
Цена: 1000
"""

# 2 способ
format2 = 'Название: {}\nЦена: {}'
print(format2.format('Iphone 16', 1200))
print(format2.format('Молоко', 100))

# 3 способ
format3 = 'Название: %s\nЦена: %s'
print(format3 % ('Iphone15', 1200))
"===========================================Методы строк=========================================="
# Методы - функции, которые относятся к определенному типу данных (классу), к ним мы обращаемся через точку
# dir() - функция, которая позволяет посмотреть все методы класса

print(dir(str))

# string.upper() - переводит все символы строк в верхний регистр
print('hello'.upper()) # HELLO

# string.lower() - переводит все символы строки в нижний регистр
print('HELLO'.lower()) # hello

# string.swapcase() - метод, который переводит регистр символов строки в противоположный
print('hELLo'.swapcase()) # HellO

# string.title() - делает первую букву каждого слова заглавной
print('hello world'.title()) # Hello World

# string.capitalize() - делает заглавной только первую букву первого слова
print('hello world'.capitalize()) # Hello world


# string.count() - считает количество вхождений заданного элемента в строку
print('hello world, this is ADA Courses'.count('l')) # 3
print('hello world, this is ADA Courses'.count('hello world, this is ADA Courses')) # 1

# string.startswith() - метод, который проверяет, начинается строка с заданного элемента
print('hello world'.startswith('h')) # True
print('hello world'.startswith('hello')) # True

# string.endswith() - метод, который проверяет, заканчивается ли строка с заданного элемента
print('hello world'.endswith('hello')) # False
print('hello world'.endswith('hello world')) # True

# string.islower() - проверяет, находится ли вся строка в нижнем регистре
print('hello world'.islower()) # True
print('hello World'.islower()) # False

# string.isupper() - проверяет, находится ли вся строка в верхнем регистре
# string_ = input('Введи строку: ')
# print(string_.isupper()) # False

# string.isdigit() - проверяет, состоит ли строка полностью из чисел
print('1234'.isdigit()) # True
print('1234k'.isdigit()) # False

# string.isalpha() - проверят, состоит ли строка полностью из букв
print('hello'.isalpha()) # True
print('hello0'.isalpha()) # False

# string.isalnum() - проверяет, состоит ли строка полностью из букв и цифр
print('2134hello'.isalnum()) # True
print('123 hello'.isalnum()) # False
print('1'.isalnum()) # True


# string.strip() - метож который полностью удаляет все пробелы с начала, и с конца строки, середину не трогает
string1 = '                         hel lo                    '
print(len(string1.strip()))# 6
print(len(string1)) # 51

# string.rstrip() - убирает все пробелы справа
print(len('hello                               '.rstrip())) # 5
print(len('hello                               ')) # 36

# string.lstrip() - убирает все пробелы слева 
print('                  hello'.lstrip())

