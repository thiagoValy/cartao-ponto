
def linha(tam=42):
    print('=' * tam)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    cont = 1
    for item in lista:
        print(f"{cont} = {item}")
        cont = cont + 1
   



