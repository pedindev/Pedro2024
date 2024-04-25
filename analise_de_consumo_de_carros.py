quantidade = int(input("Quantos carros vai analizar? "))
carros = []
consumos = []
for j in range(quantidade):
    carro = input(f"Modelo do carro {j + 1}: ")
    consumo = float(input(f"Qunatos quilimêtros o carro {j + 1} roda por litro? "))
    carros.append(carro)
    consumos.append(consumo)


distância = 1000
preço = 2.25
lista_de_consumos = []
lista_de_preços = []
carro_mais_economico = consumos.index(max(consumos))
print("Comparativo de Consumo de Combustível\n")
for i in range(len(carros)):
    litros_necessários = 1000/consumos[i]
    custo_total = litros_necessários * preço
    lista_de_consumos.append(litros_necessários)
    Output1 = ["%.2f" % elem for elem in lista_de_consumos]
    lista_de_preços.append(custo_total)
    Output2 = ["%.2f" % elem for elem in lista_de_preços]

    print(f'{i + 1} - {carros[i]} - {consumos[i]}km - {Output1[i]}l - R${Output2[i]}')


print(f'O menor consumo é do {carros[carro_mais_economico]}')
