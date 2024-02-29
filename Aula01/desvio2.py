n1 = input("Digite a primeira nota do aluno:\n")
n2 = input("Digite a segunda nota do aluno:\n")
n3 = input("Digite a terceira nota do aluno:\n")
n4 = input("Digite a quarta nota do aluno:\n")
rs = ( float(n1)+float(n2)+float(n3)+float(n4) ) / 4

print("A média do aluno é ",rs)

if (rs >= 7):
    print("Aluno está Aprovado")
elif (rs <=4):
    print("Aluno está Reprovado")
else:
    print("Aluno está em Recuperação")