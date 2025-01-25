import json
from informacoes import *


def createfile(name):
    #Salva as infomações do dia de trabalho de trabalho em arq
    dici = dicio()
    print(dici)
    a=  open('daywork.json', 'w') 
    json.dump(dici, a)
    a.close()
    print("Arquivo criado com sucesso")
        
    