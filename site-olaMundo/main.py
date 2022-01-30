from re import U


arquivo = open("log.txt","r",encoding="UTF-8")
def Registro(_arquivo):
    registro = list()
    for linha in _arquivo:
        registro.append(linha.split("\t"))
    return registro

def Listanome(registro):
    nomeList = list()
    for elemento in registro:
        if elemento[1] not in nomeList:
            nomeList.append(elemento[1])
    return nomeList


def main():

    lista_nome = Listanome(Registro(arquivo))
    for nome in lista_nome:
        print(nome) 

main()