a=5
b=10
c=0
print(f"Valor inicial, A= {a} e B= {b}")
troca= input("Deseja trocar os valores? s ou n ")
if troca=="s" :
    c=a
    a=b
    b=c
    print(f"Valor final, A= {a} e B= {b}")
else:
    print(f"Valor final, A= {a} e B= {b}")
