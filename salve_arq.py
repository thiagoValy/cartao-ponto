import json

from informacoes import *


def createfile(name):
    arq = 'daywork.csv'
    #Salva as infomações do dia de trabalho de trabalho em json
    nome = name
    projecty =  projecti()
    users = {projecty:{'name': nome, 'date': date_start().strftime('%d/%m/%Y'), 'start':date_start().strftime('%H:%M'), 'finish':finish().strftime('%H:%M')}}
    with open(arq, 'w') as file:
        json.dump(users, file)

        

   
        
            
