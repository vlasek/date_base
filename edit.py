def edit_file(file):         # метод примает путь к файлу

    with open(file, 'r', encoding='utf-8') as data:
        c: str = ''
        for i in data:
            c += i
        lst = c.split('\n')
    return lst


def del_el(id, position, txt):  # метод принимает номер строки, позицию заменяемого эл. и новые данные
    r = edit_file()
    for i in range(len(r)):
        if id == i:
            ttr = r[i].split()
            for j in range(len(ttr)):
                if j == position:
                    ttr[j] = txt+" "
            r[i] = ' '.join(ttr)
    return ' \n'.join(r)




