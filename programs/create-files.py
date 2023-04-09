import os

def create_files(file_names):
    """
    Функция создает файлы с указанными именами в текущей директории и записывает в них содержимое.

    Аргументы:
    file_names (list): Массив строк с названиями файлов.

    """
    for file_name in file_names:
        file_path = os.path.join(os.getcwd(), file_name + '.py') # Формируем полный путь к файлу
        with open(file_path, 'w') as file: # Открываем файл для записи
            file.write('"""\n\n"""\n\n# tags: \n# kyu: 6') # Записываем содержимое в файл

# Пример вызова функции с массивом названий файлов
file_names = ['decode-the-morse-code', 'playing-with-digits', 'equal-sides-of-an-array', 'detect-pangram', 'find-the-unique-number', 'split-strings', 'find-the-missing-letter', 'sort-the-odd', 'build-tower', 'highest-scoring-word', 'delete-occurrences-of-an-element-if-it-occurs-more-than-n-times', 'count-the-smiley-faces', 'build-a-pile-of-cubes', 'valid-braces', 'is-a-number-prime', 'consecutive-strings', 'write-number-in-expanded-form', 'are-they-the-same', 'break-camelcase', 'which-are-in', 'bouncing-balls', 'the-supermarket-queue', 'mexican-wave', 'count-characters-in-your-string', 'take-a-number-and-sum-its-digits-raised-to-the-consecutive-powers-and-eureka', 'two-sum', 'roman-numerals-encoder', 'roman-numerals-decoder', 'simple-encryption-1-alternating-split', 'camelcase-method']
create_files(file_names)