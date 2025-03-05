from collections import ChainMap
from interface import *
from informacoes import *
from salve_arq import *



arq = 'daywork.csv'

file ='diatrabalho.json'
cabecalho("MENU")
menu(['Iniciar Dia ', 'Encerrar Dia', 'Verificar Ponto', 'Sair'])
while True:
    caso = int(input("opção: "))
    if caso == 1:
        dict()
        
    elif caso == 2:
        fday()
        createfile()

    elif caso == 3:
        print(dicio())
       
    elif caso == 4:
        print("Sair do Sistema")
        break    

    else:
        print("Digite uma opção Válida")
            