print("Olá queremos te ajudar a viver mais e gastar menos, responda o questionário abaixo!")
tempo = float(input("Há quantos anos você fuma?: "))
customaco = float(input("Me informe quanto custa um maço de cigarros em reais: R$ "))
volumedia = float(input("Quantos maços de cigarros você fuma por dia?: "))

#calculos:
valor_gasto = float(tempo) * 365 * (customaco) * (volumedia)
if valor_gasto <= 20000:
    print("Com o valor R$ {:.2f},você poderia ter dado entrada em um carro.".format(valor_gasto))
elif valor_gasto <=50000:
    print("Com o valor R$ {:.2f}, você poderia ter comprado um carro popular usado.".format(valor_gasto))
else:
    print("Com o valor R$ {:.2f}, você poderia ter comprado um carro zero.".format(valor_gasto))
