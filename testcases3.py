import os

testcases_dir = "C:\\testcases2\\_res\\"
out_dir = "C:\\testcases2\\_complex\\"

for plik in os.listdir(testcases_dir):
    podzial=plik.find('DataOPT')
    nazwa_katalogu = plik[0:podzial]
    nazwa_pliku = plik[podzial:].replace('.txt','')

    f = open(testcases_dir+plik)
    for line in f:
        if line.find('(complex)') != -1:
            print line
