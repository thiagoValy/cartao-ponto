from interface import *
from informacoes import *

cabecalho("MENU")
menu(['Iniciar Dia ', 'Encerrar Dia', 'Verificar Ponto', 'Sair'])
while True:
    caso = int(input("opção: "))
    if caso == 1:
        nome()
        projecti()
        date_start()
    elif caso == 2:
        finish()
    elif caso == 3:
        dict()
        
    elif caso == 4:
        print("Sair do Sistema")
        break    
    else:
        print("Digite uma opção Válida")
            