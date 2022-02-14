def overwriting_file(file):
    with open('file.txt', 'w', encoding='utf-8') as data:
        data.write(file)
