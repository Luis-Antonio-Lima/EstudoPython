n = [1,2,3,4,5,6,7,8,9,10]
numero = int(input("Digite um número: "))

for num in n:
    if num == numero:
        print(f"O número {numero} está na lista")
        break
else:
    print("O número {numero} não está na lista")