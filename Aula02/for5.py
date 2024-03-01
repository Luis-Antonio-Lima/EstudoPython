n = [1,2,3,4,5,6,7,8,9,10]

print("Os números deverão ser separados por virgulas\n")
numero = input("Digite um ou mais de um número: ")

numero = [int(num.strip()) for num in numero.split(",")]

for num in numero:
    if num in n:
        print(f"{num}")
    else:
        print(f"O número {num} é inexistente")
