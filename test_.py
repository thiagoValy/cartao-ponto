
def criar_dicionario():
    return {'nome': 'Alice', 'idade': 30}

def usar_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(f'{chave}: {valor}')

# Uso das funções
dicionario = criar_dicionario()
usar_dicionario(dicionario)

