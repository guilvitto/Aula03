valor_gasolina= 5.8
valor_etanol=4.9
valor_total=0
litros=float(input("Quantos litros de combustível vc quer? "))
tipo=input("Vc quer Gasolina(g) ou Etanol(e)? ")
if tipo=="g" or tipo=="G":
    valor_total= valor_gasolina*litros
else:
    if tipo=="e" or tipo=="E":
        valor_total = valor_etanol*litros
    else:
        print("Tipo de combustível inválido")
print(f"Você escolheu {litros:.0f}L, seu valor total foi de: R$ {valor_total:.0f}")