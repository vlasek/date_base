import overwrite


def edit_file():

    with open('file.txt', 'r', encoding='utf-8') as data:
        c: str = ''
        for i in data:
            c += i
        lst = c.split('\n')
    return lst


def del_el(id, position, txt):
    r = edit_file()
    for i in range(len(r)):
        if id == i:
            ttr = r[i].split()
            for j in range(len(ttr)):
                # print(r[i][j])
                if j == position:
                    ttr[j] = txt+" "

            r[i] = ' '.join(ttr)

    return ' \n'.join(r)


overwrite.overwriting_file(del_el(4, 3, '1950'))
# print(del_el(2, 3, '1800'))
