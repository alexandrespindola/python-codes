codigo_peca1, numero_peca1, valor_peca1 = input().split()
codigo_peca2, numero_peca2, valor_peca2 = input().split()
print('VALOR A PAGAR: R$ {:.2f}'.format(int(numero_peca1) * float(valor_peca1) + int(numero_peca2) * float(valor_peca2)))