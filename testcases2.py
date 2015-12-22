import os

naglowki = []

testcases_dir = "C:\\testcases2\\"
file = 'test1.txt'

f = open(testcases_dir + file, "r")
for index, line in enumerate(f):
    if 0 == index:
        naglowki = line.split('\t')
    if 0 != index:
        line_splitted = line.split('\t')
        f_out = open(testcases_dir + '_res\\' + line_splitted[0] + '.txt', 'wb')
        for num, field in enumerate(line_splitted):
            if 0 != num:
                naglowek_czysty = naglowki[num].split(',')[0]
                ile_spacji = naglowki[num].split(',')[1]
                if field != 'null'  and field != 'null\n':
                    if num < len(line_splitted)-1:
                        f_out.write(naglowek_czysty + ' ' * int(ile_spacji) + field+ '\n')
                    else:
                        f_out.write(naglowek_czysty + ' ' * int(ile_spacji) + field)
