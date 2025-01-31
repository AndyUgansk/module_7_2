def custom_write(file_name, strings):
    # Создаем пустой словарь для сохранения позиций и строк
    strings_positions = {}

    # Открываем файл в режиме записи с указанием кодировки utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        # Перебираем строки и соответствующие им индексы
        for line_number, string in enumerate(strings, start=1):
            # Получение текущей позиции в файле, которая соответствует началу записи строки
            byte_position = file.tell()
            # Записываем строку с добавлением символа новой строки
            file.write(string + '\n')
            # Добавляем запись в словарь: ключ - кортеж (номер строки, позиция), значение - строка
            strings_positions[(line_number, byte_position)] = string

    # Возвращаем словарь с информацией о позициях строк
    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# Вызов функции и вывод результата
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
