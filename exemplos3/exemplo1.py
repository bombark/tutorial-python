





f=open("rodolfo.txt", "r")

for linha in f:
	#linha = f.readline()
	print(linha)

with open(“rodolfo.txt”) as file:
	print(linha)

f.close()
