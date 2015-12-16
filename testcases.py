import os

params = []
wykluczone = ['-5003808', '-5003812', '-5011058', '-5011090', '-5249234', '-5252854', '-5252855', '-5256484', '0',
              '2045601', '2058616', '955909', '957441', '957444', '957446', '957952', '960519', '960520', '960521',
              '961025', '961539', '966145', '966148', '968194', '968195', '968196', '968705']


def f1(seq):
    # not order preserving
    set = {}
    map(set.__setitem__, seq, [])
    return set.keys()


for katalog in os.listdir("C:\\testcases2\\_all\\"):
    for plik in os.listdir("C:\\testcases2\\_all\\" + katalog):
        if not plik.find('DataOPT.dat') == -1:
            f = open("C:\\testcases2\\_all\\{0}\\{1}".format(katalog, plik), "r")
            for line in f:
                if not line[0] == ' ':
                    koniec = line.find(' ')
                    if line[0:koniec] not in wykluczone:
                        params.append(line[0:koniec])
params = f1(params)
# params.sort()
print params
