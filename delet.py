def edit_file():

    with open('file.txt', 'r', encoding='utf-8') as data:
        c: str = ''
        for i in data:
            c += i
        lst = c.split('\n')
    return lst


def del_el(id):
    r = edit_file()
    for i in range(len(r)):
        if id == i:
            r.pop(i)
        r[i-1] += '\n'
    return ''.join(r)


