import shutil
import os

for katalog in os.listdir('C:\\testcases2\\_all\\'):
    for plik in os.listdir('C:\\testcases2\\_all\\' + katalog):
        if not plik.find('DataOPT.dat') == -1:
            nowa_nazwa = 'C:\\testcases2\\_src\\' + katalog + '_' + plik + '.txt'
            shutil.copy2('C:\\testcases2\\_all\\'+katalog+'\\'+plik, nowa_nazwa)
