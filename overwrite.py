def overwriting_file(dt): # принимает результат изменения данных 
    with open('Путь к файлу', 'w', encoding='utf-8') as data:
        data.write(dt) # перезаписывает файл с новыми данными
