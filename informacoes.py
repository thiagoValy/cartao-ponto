from datetime import datetime
from datetime import time
from collections import ChainMap


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


def fday():
    global users
    #funcao cria um dicionario de fim do trabalho
    fim = {}
    finish()
    nome = name
    projecty = project
    users={projecty :{'name': nome, 'date': date_start().strftime('%d/%m/%Y'), 'start':date_start().strftime('%H:%M'), 'finish':finish().strftime('%H:%M')}}
    return users


def dict():
    #Funcao cria um dicionario par iniciar o trabalho
    global users
    users = {}
    date_start()
    nome()
    projecti()
    date_start()
    finish()
    users={project: {'name': nome, 'date': date_start().strftime('%d/%m/%Y'), 'start':date_start().strftime('%H:%M')}}
    return users


def dicio():
    global users
    fday()
    nome = name
    projecty = project
    users[projecty] = {'name': nome, 'date': date_start().strftime('%d/%m/%Y'), 'start':date_start().strftime('%H:%M'), 'finish':finish().strftime('%H:%M')}
    return users