carro = 60.00;
km = 0.15;
diasAlugados = int(input('quantos dias alugados: '))
KmRodado = float(input('quantos km rodados: '))
valorTotal = (carro * diasAlugados) + (KmRodado * km)

print('valor das diarias:RS{}' .format(valorTotal))