from datetime import datetime
from datetime import time



def nome():# usuario ira digitar seu nome e projeto.
    global name
    name = str(input("Digite seu nome: "))
    return name
    
def projecti():
    global project
    project = str(input("Qual o projeto que esta trabalhando: ")) 
    return project
    


def date_start():#sistema já registra o dia
    date = datetime.today()
    return date
      


def finish():# Ao findar o dia de trabalho a sistema registra o dia e a hora que terminou o dia de trabalho.
    date_start()
    hour_finish = datetime.now()
    return hour_finish


def dict():
    users ={} 
    nome = name
    projecty = project
    date_start()
    finish()
    users[projecty] = {'name': nome, 'date': date_start(),'finish': finish() }
    print(f"{name.title()} iniciou o projeto {projecty.title()} às {date_start().strftime('%H:%M')} no dia {date_start().strftime('%d/%m/%Y')} ")
    
    return users

  
    







