valor = float(input('digite o valor: R$'))
desconto = 15.0;
valorComDesconto = valor + (valor * desconto / 100);
print('o valor com almento de {}% é : R${:.2f}' . format(desconto, valorComDesconto))