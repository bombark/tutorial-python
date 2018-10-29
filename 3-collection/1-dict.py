print("\n   1) criando um dicionario")
A = { "name": "dicionario" }
print(A)


print("\n   2) adicionando os item idade: 20, score: 1050.33 e descricao: 'bacana'")
A["idade"] = 20
A["score"] = 1050.33
A["descricao"] = "bacana"
print(A)


print("\n   3) removendo o item idade do dicionario")
del(A["idade"])
print(A)


print("\n   4) Quanto itens tem no dicionario?")
print( len(A) )


print("\n   5) iterando os itens do dicionario")
for key,val in A.items():
	print(key,val)


print("\n   6) verificando a existencia do index 'descricao' no dicionario")
if "descricao" in A:
	print("presente")
else:
	print("nao presente")


print("\n   7) apagando uma lista")
A = {}
print(A)
