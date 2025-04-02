t1=input("Digite o time 1: ")
gt1=int(input("Digite os gols do time 1: "))
t2=input("Digite o time 2: ")
gt2=int(input("Digite os gols do time 2: "))

print(f"")
if gt1==gt2:
    print(f'Deu empate!!')
else :
    if gt1<gt2:
        print(f'O {t2} ganhou do(a) {t1}!!')
    else:
        print(f'O {t1} ganhou do(a) {t2}!!')
