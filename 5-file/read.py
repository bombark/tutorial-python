print ("Lendo o arquivo inteiro")
fd1=open("rodolfo.txt", "r")
texto = fd1.read()
fd1.close()
print(texto)


print ("\nLendo o arquivo usando o bloco with")
with open("rodolfo.txt") as fd3:
	print( fd3.read() )
fd3.close()


print ("\nIterando linha por linha")
fd2=open("rodolfo.txt", "r")
for linha in fd2:
	print("i: "+linha)
fd2.close()


print ("\nIterando linha por linha usando with")
with open("rodolfo.txt") as fd4:
	for linha in fd4:
		print("i: "+linha)
fd4.close()
