"""Игра Hangman"""
import random


def random_word():
    """Выдает рандомное слово из файла"""
    with open('text.txt', 'r', encoding='utf-8') as file_text:
        choose_word = file_text.read().strip().split()
    r_word = random.choice(choose_word)
    return r_word


def menu():
    """Функция Меню для выбора действий"""
    try:
        print("1 - Начать игру\n2 - Посмотреть прошлые слова\n3 - Выйти")
        start_word = input("Введите число: ")  # цифра с меню игры
        if start_word == '1':  # начало игры
            game()
        elif start_word == '2':  # список слов
            with open('used_words.txt', 'r', encoding='utf-8') as f:
                line = f.readline()
            ilne = list(line.strip().split())
            if len(ilne) == 1:
                print("Список пуст")
            else:
                for i in range(len(ilne)-1):
                    print(ilne[i])
            if restart_game():
                menu()
            else:
                print('До встречи! Пока!!!')
                exit_from_game()
        elif start_word == '3':  # выход из игры
            exit_from_game()
        else:
            print("\nВведите нужную цифру!!!")
            menu()
    except ValueError:
        print("\nВведите нужную цифру!!!")
        menu()


def game(attempts=10):
    """Процесс игры"""
    used_letters = set()  # множество использованных слов

    while True:

        print("Количество попыток: %d" % attempts)  # count attempts
        print('Доступные буквы: ' + ' '.join(alphabet))  # alphabet
        hidden_word = str(' '.join(guessed))  # вывод скрытого слова
        print(hidden_word)
        char = input("Введите букву: ").strip(' ')

        if char in splite_word:

            if char in used_letters:
                print("Буква уже была использована!!!")
            elif char not in alphabet1:
                print("Введите букву русского алфавита!!!")
            else:
                for index, value in enumerate(splite_word):  # цикл  изменения _ на букву
                    if value == char:
                        guessed[index] = char
                        used_letters.add(char)
        elif char not in alphabet1:
            print("Введите букву русского алфавита!!!")
            print("\nИспользованные буквы: " + ' '.join(used_letters))
            continue
        else:
            attempts -= 1  # уменьшение кол-ва попыток
        used_letters.add(char)  # добавление буквы в множество использованных букв
        print("\nИспользованные буквы: " + ' '.join(used_letters))  # перечень введенных букв
        if char in alphabet:
            alphabet.remove(char)  # удаление буквы из предложенных

        if attempts == 0:  # условие поражения
            print('Вы проиграли!!!')
            print("Загаданное слово: " + (''.join(splite_word)))
            if restart_game():
                menu()
            else:
                print("Игра завершена!!!")
                exit_from_game()
            break


def exit_from_game():
    """Выход из игры"""
    raise SystemExit(1)


def restart_game():
    """Перезапуск игры"""
    print('Хотите продолжить? (да или нет)')
    return input().lower().startswith('д')


def add_word(some_word):
    """Добавление слова в файл"""
    with open('used_words.txt', 'a', encoding='utf-8') as file:
        for index in some_word:
            file.write(index + ' ')


alphabet = list(map(chr, range(ord('а'), ord('я')+1)))  # для отображения букв
alphabet1 = list(map(chr, range(ord('а'), ord('я')+1)))  # для отображения букв
word = random_word()  # результат метода random_word
used_words = []
used_words.append(word)  # добавление использованых слов в список
splite_word = list(word)  # разделить слово на буквы
guessed = ['_' for i in splite_word]  # вставляем пробелы вместо слова
add_word(used_words)  # запись слов в файл
menu()
