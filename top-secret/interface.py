from os import system
from pathlib import Path
from tkinter import*

from alphabets import LatinAlphabet, CyrillicAlphabet
from caesar import CaesarCoder, CaesarDecoder, CaesarAutoDecoder
from vernam import VernamCoder, VernamDecoder
from vigenere import VigenereCoder, VigenereDecoder


class Interface:
    def __init__(self):
        print("Это приложение для шифровки и дешифровки текстов. Выберите язык:\nru - кириллица\nen - латиница")
        language = input()
        while language != 'ru' and language != 'en':
            language = input("Неправильный формат. Выберите язык повторно\n")
        if language == 'ru':
            self.alphabet = CyrillicAlphabet
        else:
            self.alphabet = LatinAlphabet

        self.path_for_read = Path(input("Введите путь до файла с текстом\n"))
        while not self.path_for_read.exists() or not self.path_for_read.is_file():
            if not self.path_for_read.exists():
                self.path_for_read = Path(input("Путь некорректен. Повторите ввод\n"))
            else:
                self.path_for_read = Path(input("Вы указали путь не на файл. Повторите ввод\n"))

        self.path_for_write = Path(input("Введите путь до файла для записи\n"))

        print("Выберите сценарий:\n1 - шифровка\n2 - дешифрофка")
        option = input()
        while option != '1' and option != '2':
            option = input("Неправильный формат. Повторите ввод\n")
        if option == '1':
           self.run_coding_scenario()
        else:
           self.run_decoding_scenario()

    def run_coding_scenario(self):
        print("Выберите шифр:\n1 - цезаря\n2 - виженера\n3 - вернама")
        number = input()
        while number != '1' and number != '2' and number != '3':
            number = input("Неправильный формат. Повторите ввод\n")
        if number == '1':
            self.code_object = CaesarCoder
            key = input("Введите целое неотрицательное число (ключ для шифрования)\n")
            while True:
                try:
                    key = int(key)
                    if (key < 0):
                        key = input("Неправильный формат. Введите целое неотрицательное число\n")
                    else:
                        break
                except:
                    key = input("Неправильный формат. Введите целое неотрицательное число\n")
            self.key = key
        elif number == '2':
            self.code_object = VigenereCoder
            self.key = input("Введите строку (ключ для шифрования)\n")
        else:
            self.code_object = VernamCoder
            self.key = input("Введите строку (ключ для шифрования)\n")

        with open(self.path_for_read, 'r') as readfile, open(self.path_for_write, 'w') as writefile:
            writefile.write(self.code_object.code(readfile.read(), self.key))

    def run_decoding_scenario(self):
        print("Выберите шифр:\n1 - цезаря\n2 - виженера\n3 - вернама")
        number = input()
        while number != '1' and number != '2' and number != '3':
            number = input("Неправильный формат. Повторите ввод\n")
        if number == '1':
            print("Если ваш текст достаточно длинный, я могу попробовать дешифровать его автоматически\n"
                  "Хотите попробовать?\n"
                  "1 - да\n"
                  "2 - нет")
            decoding_type = input()
            while decoding_type != '1' and decoding_type != '2':
                decoding_type = input("Неправильный формат. Повторите ввод\n")
            if (decoding_type == '1'):
                self.decode_object = CaesarAutoDecoder
                key = 0
            else:
                self.decode_object = CaesarDecoder
                key = input("Введите целое неотрицательное число (ключ для дешифровки)\n")
                while True:
                    try:
                        key = int(key)
                        if (key < 0):
                            key = input("Неправильный формат. Введите целое неотрицательное число\n")
                        else:
                            break
                    except:
                        key = input("Неправильный формат. Введите целое неотрицательное число\n")
            self.key = key
        elif number == '2':
            self.decode_object = VigenereDecoder
            self.key = input("Введите строку (ключ для дешифровки)\n")
        else:
            self.decode_object = VernamDecoder
            self.key = input("Введите строку (ключ для дешифровки)\n")
        with open(self.path_for_read, 'r') as readfile, open(self.path_for_write, 'w') as writefile:
            writefile.write(self.decode_object.decode(readfile.read(), self.key))










