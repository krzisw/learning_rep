import os

testcases_dir = "C:\\testcases2\\_all\\"
parametry_zlozone = ['FREE_FLIGHT_WPT', 'NO_CTLG_COST', 'NO_EXCLUDED_AIRSPCS', 'NO_EXCL_CNTRY_TR', 'NO_EXCL_SEGM_TR',
                     'NO_SUB_ROUTES', 'NUMBER_MINI_OFP', 'NUM_ADD_COST_INDEX', 'NUM_SUIT_ENR_ALTN']
params = []
all_params = [[], []]
sum_params = []
x = 0
odstep = 0

f_out = open("C:\\testcases2\\test.txt", 'w')
x = -1
for katalog in os.listdir(testcases_dir):
    for plik in os.listdir(testcases_dir + katalog):
        if not plik.find('DataOPT.dat') == -1:
            f = open(testcases_dir + katalog + '\\' + plik, "r")
            x += 1
            all_params.append([])
            for line in f:
                for parametr_zlozony in parametry_zlozone:
                    if line.find(parametr_zlozony) != -1:
                        koniec = line.find(' ')
                        wartosc_parametru = line[koniec:]
                        wartosc_parametru = int(wartosc_parametru.strip(' '))
                        for _ in xrange(wartosc_parametru):
                            next(f)
                koniec = line.find(' ')
                odstep = (line.rfind(' ') - line.find(' ')) + 1
                all_params[x].append(line[0:koniec] + ',' + str(odstep))
                f_out.write(line[0:koniec])
            f_out.write(katalog + '\n')

for row in all_params:
    prev_param = ''
    for field in row:
        if len(sum_params) == 0:
            sum_params.append(field)
        else:
            for param in sum_params:
                if field not in sum_params:
                    sum_params.insert(sum_params.index(prev_param) + 1, field)
        prev_param = field
    del prev_param
print sum_params
