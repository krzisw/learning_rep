import os
test_plik = open('C:\\testcases2\\porownanie.txt', "w")
for katalog in os.listdir("C:\\testcases2\\_all\\"):
    for plik in os.listdir("C:\\testcases2\\_all\\" + katalog):
        if not plik.find('DataOPT.dat') == -1:
            f = open("C:\\testcases2\\_all\\{0}\\{1}".format(katalog, plik), "r")
            for line in f:
                splited_line = line.split()
                prev = ''
                if splited_line.__len__() == 2:
                    prev = splited_line[0]
                    test_plik.write(splited_line[0]+'|')
            test_plik.write('\n')
