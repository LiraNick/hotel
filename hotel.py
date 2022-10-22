from datetime import datetime
from time import sleep 
from controller import *

def menu():
    print(("="*20),"Hotel Transilvânia ", ("="*20))
    #menu
    menu=1
    agora=datetime.now(tz=None)
    if agora.hour >=5 and agora.hour<13:
        print("\nBom dia")
    if agora.hour >=13 and agora.hour<18:
        print("\nBoa tarde")
    else:
        print("\nBoa noite")
    while(menu!=0):
        print("Por Favor Escolha a opção desejada:\n")
        menu=int(input("1.Fazer checkin\n2.Relatorio Clientes\n3.Procurar hospedes\n4.Fazer checkout\n0.Finalizar atendimento\noperacao>:"))
        match menu:
                case 1:
                    cliente = {}
                    cliente['Nome'] = str(input('Seu nome: '))
                    cliente['sobreNome'] = str(input('Seu sobrenome: '))
                    cliente['idade'] = int(input('Sua idade: '))
                    cliente['cpf'] = int(input('Seu cpf: '))
                    checkin(cliente)
                case 2:
                    relatorio()
                case 3:
                    clienteFind=str(input("Digite o nome desejado:"))
                    procurar(clienteFind)
                case 4:
                    clienteFind=str(input("Digite o nome desejado:"))
                    fazerCheckout(clienteFind)
                case _:
                    print("valeu cachorro ate uma proxima!")
menu()
print("vlw :)")