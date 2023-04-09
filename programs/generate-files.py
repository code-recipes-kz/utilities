import os
import re

def clean_label(s):
    s = s.lower()  # Преобразуем строку к lower case
    s = s.replace(" ", "-")  # Заменяем пробелы на "-"
    s = s.replace("_", "-")  # Заменяем знаки "_" на "-"
    s = re.sub(r'[^\w-]', '', s)  # Удаляем все знаки препинания, кроме "-", "_" и буквенно-цифровых символов
    s = re.sub(r'(-{2,})', '-', s)  # Убираем повторяющиеся символы "-"
    return s

def clean_tag(tag):
    # Приводим первую букву к верхнему регистру, остальные - к нижнему регистру
    tag = tag.lower()
    tag = tag.capitalize()
    return tag

def generate_files(objects):
    for obj in objects:
        label = obj['label']
        # Очищаем значение поля label
        label = clean_label(label)
        tags = obj['tags']
        # Очищаем и преобразуем значения полей tags
        cleaned_tags = [clean_tag(tag) for tag in tags]
        tags_str = ', '.join(cleaned_tags)
        # Создаем имя файла из очищенного значения поля label с расширением .py
        filename = f"{label}.py"
        # Создаем файл в текущей папке с именем из очищенного значения поля label и расширением .py
        with open(filename, 'w') as file:
            # Записываем содержимое файла
            file.write('"""\n\n"""\n\n')
            file.write(f"# tags: {tags_str}\n")
            file.write("# kyu: 6\n")

# Пример массива объектов
objects = [
    {
      "label": "Simple Encryption #1 - Alternating Split",
      "tags": [
        "CRYPTOGRAPHY",
        "ALGORITHMS",
        "STRINGS",
        "ARRAYS",
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "WeIrD StRiNg CaSe",
      "tags": [
        "STRINGS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Rectangle into Squares",
      "tags": [
        "FUNDAMENTALS",
        "GEOMETRY",
        "PUZZLES"
      ]
    },
    {
      "label": "Give me a Diamond",
      "tags": [
        "STRINGS",
        "ASCII ART",
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "IP Validation",
      "tags": [
        "REGULAR EXPRESSIONS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Title Case",
      "tags": [
        "STRINGS",
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "Make the Deadfish Swim",
      "tags": [
        "PARSING",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Help the bookseller !",
      "tags": [
        "FUNDAMENTALS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Good vs Evil",
      "tags": [
        "ALGORITHMS"
      ]
    },
    {
      "label": "Sums of Parts",
      "tags": [
        "FUNDAMENTALS",
        "PERFORMANCE",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Reverse or rotate?",
      "tags": [
        "ALGORITHMS",
        "STRINGS"
      ]
    },
    {
      "label": "Multiplication table",
      "tags": [
        "ARRAYS",
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "Find the missing term in an Arithmetic Progression",
      "tags": [
        "ALGORITHMS",
        "MATHEMATICS"
      ]
    },
    {
      "label": "Encrypt this!",
      "tags": [
        "FUNDAMENTALS",
        "STRINGS",
        "REGULAR EXPRESSIONS",
        "ARRAYS",
        "CIPHERS",
        "ALGORITHMS",
        "CRYPTOGRAPHY",
        "SECURITY"
      ]
    },
    {
      "label": "Meeting",
      "tags": [
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "Data Reverse",
      "tags": [
        "ARRAYS",
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "Backspaces in string",
      "tags": [
        "FUNDAMENTALS",
        "STRINGS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "A Rule of Divisibility by 13",
      "tags": [
        "FUNDAMENTALS",
        "ALGORITHMS",
        "MATHEMATICS"
      ]
    },
    {
      "label": "Consonant value",
      "tags": [
        "STRINGS",
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "Tortoise racing",
      "tags": [
        "FUNDAMENTALS",
        "MATHEMATICS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "The Vowel Code",
      "tags": [
        "ARRAYS",
        "STRINGS",
        "REGULAR EXPRESSIONS",
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "Valid Phone Number",
      "tags": [
        "REGULAR EXPRESSIONS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Triple trouble",
      "tags": [
        "ALGORITHMS"
      ]
    },
    {
      "label": "Fold an array",
      "tags": [
        "FUNDAMENTALS",
        "LOGIC",
        "MATHEMATICS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Validate Credit Card Number",
      "tags": [
        "ALGORITHMS"
      ]
    },
    {
      "label": "Street Fighter 2 - Character Selection",
      "tags": [
        "ARRAYS",
        "LISTS",
        "FUNDAMENTALS",
        "GRAPH THEORY"
      ]
    },
    {
      "label": "Playing with passphrases",
      "tags": [
        "STRINGS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Fibonacci, Tribonacci and friends",
      "tags": [
        "ARRAYS",
        "LISTS",
        "NUMBER THEORY",
        "FUNDAMENTALS"
      ]
    },
    {
      "label": "+1 Array",
      "tags": [
        "FUNDAMENTALS",
        "ARRAYS",
        "ALGORITHMS"
      ]
    },
    {
      "label": "Pyramid Array",
      "tags": [
        "ALGORITHMS"
      ]
    }
]

# Вызываем функцию для генерации файлов
generate_files(objects)