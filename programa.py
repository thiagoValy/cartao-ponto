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
        nome()
        dict()
        
    elif caso == 2:
        fday()
        
        
    elif caso == 3:
        createfile(arq)
       
        
        

    elif caso == 4:
        print("Sair do Sistema")
        break    
    else:
        print("Digite uma opção Válida")
            