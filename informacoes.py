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
    global hour_finish
    date_start()
    hour_finish = datetime.now()
    return hour_finish


def dict():
    #Funcao cria um dicionario par iniciar o trabalho
    global users
    users = {}
    date_start()
    nome = name
    projecty = projecti()
    date_start()
    finish()
    users[projecty] = {'name': nome, 'date': date_start().strftime('%d/%m/%Y'), 'start':date_start().strftime('%H:%M')}
    print(f"{name.title()} iniciou o projeto {projecty.title()} às {date_start().strftime('%H:%M')} no dia {date_start().strftime('%d/%m/%Y')} ")
    print(users)
    return users


def fday():
    global fim
    #funcao cria um dicionario de fim do trabalho
    fim = {}
    finish()
    fim = {'finish_h': hour_finish.strftime('%H:%M')}
    print(f"Dia finalizado as {hour_finish.strftime('%H:%M')}")
    print(fim)


def dicio():
    dic1 = users
    dic2 = fim
    dic1.update(dic2)
    return dic1