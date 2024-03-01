rodizio = input("Digite um número de 0 a 9, e saiba qual a semana do rodizio você não poderá sair de carro: ")
match rodizio:
    case '1' | '2':
        print("O seu carro não pode rodar na Segunda-Feira")
    case '3' | '4':
        print("O seu carro não pode rodar na Terça-Feira")
    case '5' | '6':
        print("O seu carro não pode rodar na Quarta-Feira")
    case '7' | '8':
        print("O seu carro não pode rodar na Quinta-Feira")
    case '9' | '0':
        print("O seu carro não pode rodar na Sexta-Feira")
    case _:
        print("Valor inexistente. Tente novamente")