# Pede um número e verifica se é par ou impar

numero = input("Digite um número\n")

# É necessário realizar a coversão de texto para número
# Pois a função input sempre retorna o valor em formato texto
# Então, utilizamos a função int para converter
# a variável número em valor númerico inteiro e assim realizar
# os cálculos necessários

numero= int(numero)

if(numero % 2 == 0):
    print("O número digitado é par")
else:
    print("O nuúmero digitado é impar")