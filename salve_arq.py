import json
from informacoes import *




def createfile():
    arq = 'daywork.csv'
    #Salva as infomações do dia de trabalho de trabalho em json
    dicio()
    print( dicio())
    with open(arq, 'w') as file:
        json.dump(dicio(), file)
        file.close()

            