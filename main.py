from Estacionamento import Estacionamento
from Carro import Carro

eo = 0

def main():
    run = True
    print("-------Bem vindo ao gerenciador do estacionamento!")
    x = int(input("Quantas fileiras?: "))
    y = int(input("Quantas colunas?:"))
    eo = Estacionamento(x, y)
    while run:
        print("---MENU---")
        print("-1. Adicionar carro")
        print("-2. Verificar carros estacionados")
        print("-3. Verificar meu carro")
        print("-4. Pagar estacionamento")
        print("-5. Sair")
        
        opcao = int(input("Que operação?: "))
        

        if opcao == 1:
            eo.registrarCarro()
        elif opcao == 2:
            eo.ApresentarCarros()
        elif opcao == 3:
            placa = input("Informe a placa: ")
            eo.printCarros(placa)
        elif opcao == 4:
            placa = input("Informe a placa do carro a ser retirado: ")
            eo.retirarCarro(placa);
        elif opcao == 5:
            print("Adeus!")
            break
        else:
            print("Opção invalida!")
            
        print("----------")

main()