
print("\n   1) criando uma lista")
A = [20,10,15]
print(A)


print("\n   2) adicionando os items 40, 34.44 e 'texto qualquer' na lista A")
A.append(40)
A.append(34.44)
A.append("texto qualquer")
print(A)


print("\n   3) removendo o item 40 da lista")
A.remove(40)
print(A)


print("\n   4) Quanto itens tem na lista?")
print( len(A) )


print("\n   5) inserindo a string 'aqui' na posicao 2 da lista")
A.insert(2,'aqui')
print( A )


print("\n   6) iterando os itens de uma lista")
for item in A:
	print(item)


print("\n   7) ordenando os itens de uma lista")
A.sort()
print(A)


print("\n   8) apagando uma lista")
A = []
print(A)
