preco = float(input('digite o preço: R$'))
desconto = 5.0;
valorComDesconto = preco - (preco*desconto/100);
print('o pre com desconto de {}% é : R${:.2f}' . format(desconto, valorComDesconto))