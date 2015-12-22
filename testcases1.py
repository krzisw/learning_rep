import os
import headers

testcases_dir = "C:\\testcases2\\_all\\"
parametry_zlozone = ['FREE_FLIGHT_WPT', 'NO_CTLG_COST', 'NO_EXCLUDED_AIRSPCS', 'NO_EXCL_CNTRY_TR', 'NO_EXCL_SEGM_TR',
                     'NO_SUB_ROUTES', 'NUMBER_MINI_OFP', 'NUM_ADD_COST_INDEX', 'NUM_SUIT_ENR_ALTN']

def znadz_wartosc(file, naglowek):
    naglowek_czysty = naglowek.split(',')[0]
    f = open(testcases_dir + katalog + '\\' + file, "r")
    found = 'null'
    for line in f:
        koniec = line.find(' ')
        if line[0:koniec] == naglowek_czysty:
            print line+'| |'+naglowek_czysty+'| |'+str(line.find(naglowek_czysty))
            found = line[koniec:]
            found = found.strip(' ')
            found = found.strip('\n')
            for parametr_zlozony in parametry_zlozone:
                if line.find(parametr_zlozony) != -1:
                    found = line[koniec:]
                    found = found.strip(' ')
                    found = found.strip('\n')
                    if found != '0':
                        found = found +'(complex)'
            break
    return found


naglowek = ''
linia = ''

f_out = open("C:\\testcases2\\test1.txt", 'w')
f_out.write('TC_NAME'+'\t')
for idx, naglowek in enumerate(headers.naglowki):
    if idx < len(headers.naglowki)-1:
        f_out.write(naglowek+'\t')
    else:
        f_out.write(naglowek)
f_out.write('\n')

for katalog in os.listdir(testcases_dir):
    for plik in os.listdir(testcases_dir + katalog):
        if not plik.find('DataOPT.dat') == -1:
            f_out.write(katalog + '_' + plik+'\t')
            for idx, naglowek in enumerate(headers.naglowki):
                linia = znadz_wartosc(plik, naglowek)
                if idx < len(headers.naglowki)-1:
                    f_out.write(linia+'\t')
                else:
                    f_out.write(linia)
            f_out.write('\n')

