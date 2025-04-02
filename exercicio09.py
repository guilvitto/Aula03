h1= int(input("Digite a hora1: "))
min1= int(input("Digite o min1: "))
h2= int(input("Digite a hora2: "))
min2= int(input("Digite o min2: "))

total_min= (min1+min2)
total_hora=h1+h2
if total_min>=60:
    total_hora+=1
    total_min-=60
if total_hora>=24:
    total_hora-=24
else:
    total_hora-=12
print(total_hora,total_min)