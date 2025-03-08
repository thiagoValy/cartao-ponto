from informacoes import *
from datetime import *
import os
import json
from datetime import *


arq = 'daywork.json'
caminhos = os.path.join('day_work/', arq)
def createfile():
    arq = 'daywork.json'
    caminhos = os.path.join('day_work/', arq)
    conteudo = dicio()

    if os.path.exists(caminhos):
        with open(caminhos,'r') as file:
            dados = json.load(file)
    else:
        dados = []

    dados.append(conteudo)


    with open(caminhos, 'w') as file:
        json.dump(dados, file, indent=4)

    print("Arquivo Salvo com Sucesso ")

def showinformation():
    arq = 'daywork.json'
    caminhos = os.path.join('day_work/', arq)
    with open(caminhos,'r') as file:
        dados = json.load(file)
    for item in dados:
        project = item.get('project')
        data = item.get('date')
        start = item.get('start')
        finish = item.get('finish')
        print(f"Projeto: {project}\nData: {data}\nInício: {start}\nFim: {finish}\n")

    