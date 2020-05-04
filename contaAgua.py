consumo = int(input())

valor = 0 #valor da taxa

if(consumo > 100):
    valor = valor + ((consumo - 100) * 5)
    consumo = consumo - (consumo - 100)
if(consumo > 30 and consumo <= 100):
    valor = valor + ((consumo - 30) * 2)
    consumo = consumo - (consumo - 30)
if(consumo > 10 and consumo <= 30):
    valor = valor + ((consumo - 10) * 1)
    consumo = consumo - (consumo - 10)
if(consumo <= 10):
    valor = valor + 7

print(valor)