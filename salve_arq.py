from informacoes import *
from datetime import *
import os
import json


arq = 'daywork.json'
caminho = os.path.join('day_work/', arq)
def createfile():
    arq = 'daywork.json'
    caminho = os.path.join('day_work/', arq)
    conteudo = dicio()

    if os.path.exists(caminho):
        with open(caminho,'r') as file:
            dados = json.load(file)
    else:
        dados = []

    dados.append(conteudo)


    with open(caminho, 'w') as file:
        json.dump(dados, file, indent=4)

    print("Arquivo Salvo com Sucesso ")
