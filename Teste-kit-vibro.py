print('***********************************************************************')
print('*             APLICAÇÃO CONSTRUÍDA POR: SIDNEY BISPO                  *')
print('*             PARA NIPPONFLEX USAR PARA TESTE E ANÁLISE               *')
print('*              DO KIT VIBROMASSAGEADOR DEELING-CHINA                  *')                      
print('***********************************************************************')

from datetime import datetime
today = datetime.now()
day = today.day
month = today.month
year = today.year
print ("hoje ", today, " dia ", day, "/", month, "/", year)
print ("hora ", today.hour, "| min ", today.minute, "| seg ", today.second)

nlote = str(input('Digite o número do lote: \n'))
qlote = float(input('Digite a quantidade do lote:  \n' ))
mkit = str(input('Digite o modelo do kit: Swgs ou Relax: \n'))
tpkit = str(input('Digite o tipo de kit: Maquete, Solteiro ou Único: \n'))
if (tpkit == ('Único')):
        print('Kit Único tem 10 motores! ')
elif (tpkit == ('Solteiro') or ('Maquete')):
       print('Maquete ou Solteiro tem 5 motores! ')
kites = int(input('Digite a quantidade de kits testados: \n'))
ptes = qlote*kites/1000
print('Referente a {:.1f} % da quantidade do lote: '.format(ptes))
kitdef = int(input('Digite a quantidade de kits que apresentaram defeito! \n'))
dkit = kitdef/kites*100
print('Referente a {:.1f}% da quantidade de kits testados!' .format(dkit))
motorr = int(input('Digite a quantidade de motores com ruído excessivo: \n'))
rmotor = motorr/kitdef*10
print('Referente a {:.2f}% dos kits que apresentaram defeito!'.format(rmotor))
motort = int(input('Digite a quantidade de motores travados: \n'))
tmotor = motort/kitdef*10
print('Referente a {:.2f}% dos kits que apresentaram defeito!'.format(tmotor))
motorc = int(input('Digite a quantidade de motores em curto: \n'))
cmotor = motorc/kitdef*10
print('Referente a {:.2f}% dos kits que apresentaram defeito!'.format(cmotor))



print('\nO número do lote é:\n', nlote)
print('\nA quantidade do lote é:\n{:.3f} Kits'.format(qlote))
print('\nO modelo do kit é:\n',mkit)
print('\nO tipo de kit é:\n',tpkit)
print('\nA quantidade de kits testados é:\n',kites)
print('\nO total de kits defeituosos é:\n',kitdef)
print('\nO percentual de kits com defeito é:\n{:.1f}%'.format(dkit))
print('\nA quantidade de motores com alto nível de ruído é:\n',motorr)
print('\nO percentual de motores com alto nível de ruído é:\n{:.1f}%'.format( rmotor ))
print('\nA quantidade de motores travados é:\n',motort)
print('\nO percentual de motores travados é:\n{:.1f}%'.format (tmotor ))
print('\nA quantidade de motores em curto é:\n',motorc)
print('\nO percentual de motores em curto é:\n{:.1f}%'.format(cmotor))
             



