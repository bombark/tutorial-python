

print("1.1) Definindo uma funcao com parametros A e B e retornando um resultado")

def subtracao(A,B):
	return A-B


print("1.2) Chamando a funcao subtracao com parametros A e B e retornando um resultado")

res = subtracao(15,10)
print(res)

res = subtracao(B=15,A=10)
print(res)




print("2.1) Definindo uma funcao com parametro opcional")

def subtracao_opt(A=40,B=20):
	return A-B


print("2.2) Chamando a funcao subtracao_opt com parametro opcional")
sum = subtracao_opt()
print(sum)
sum = subtracao_opt(B=30,A=60)
print(sum)
