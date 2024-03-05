def montar_tabuada(numero=0):
    arq = open ("tabuada.txt","w")
    for i in range(1,11):
        arq.write(str(numero) + " x " + str(i) + " = " + str(numero*i)+"\n")
    arq.close()
n = input("Digite um número: ")
montar_tabuada(int(n))
