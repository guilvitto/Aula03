n1=float(input("Digite sua nota 1: "))
n2=float(input("Digite sua nota 2: "))
n3=float(input("Digite sua nota 3: "))
media=(n1+n2+n3)/3
print("Sua média foi: ",media)
if media>=7:
     print("Você está APROVADO! :D")
else:
    if media < 4:
        print("Você está REPROVADO! T_T")
    else:
        print("Você está em RECUPERAÇÃO! ;_;")