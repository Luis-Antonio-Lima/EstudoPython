print("Programa que verifica se o CPF é válido")

# Variavel que guarda o cpf digitado pelo usuário
# Criar uma variável para guardar o cpf que estamos

cpf_usuario = input("Digite o seu CPF: ")
peso10 = 10
peso11 = 11
rst = 0
cpf_calc = ""

# Para obter os 9 primeiros digitos do cpf foi necessário usar uma estrutura for com uma
# contagem de 0 até 9

for i in range(0,9):

# Para calcular um digito por vez com o peso foi necessario converter cada digito em número
# inteiro depois, somamos os resultados obtidos armazenado na variavel resultado
    cpf_calc += cpf_usuario[i]

    rst+=int(cpf_usuario[i])*peso10

# Todas as vezes que o laço for rodar, será subtraido o valor 1 da variável peso10

    peso10-=1

# A variável resto, guarda o resto da divisão

resto = rst % 11

# Se o resto da divisão for menor que 2, então o primeiro digito será 0(zero)
# Caso contrário o devemos subtrair 11 pelo valor encontrado em resto

if( resto < 2 ):
    print("Primeiro digito é 0")
    cpf_calc+="0"
else:
    print("Primeiro digito é "+str(11-resto))
    cpf_calc+=str(11-resto)

# Para obter os 10 primeiros digitos do cpf foi necessário usar uma estrutura for com uma contagem de 0 até 10

rst = 0

for i in range(0,10):

# Para calcular um digito por vez com o peso foi necessario converter cada digito em número
# inteiro depois, somamos os resultados obtidos armazenado na variavel resultado

    rst+=int(cpf_usuario[i])*peso11

# Todas as vezes que o laço for rodar, será subtraido o valor 1 da variável peso11

    peso11-=1

# A variável resto, guarda o resto da divisão

resto = rst % 11

# Se o resto da divisão for menor que 2, então o primeiro digito será 0(zero)
# Caso contrário o devemos subtrair 11 pelo valor encontrado em resto

if( resto < 2):
    cpf_calc+="0"
else:
    cpf_calc+=str(11-resto)

print(cpf_calc)

# Validador do CPF
# Ele irá verificar o CPF e avisar se ele é válido ou não

if (cpf_calc == cpf_usuario):
    print("Seu CPF é Válido")
else:
    print("Seu CPF é Inválido")