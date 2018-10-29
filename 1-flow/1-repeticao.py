
print("1) Contando de 0 a 4 usando While")
a = 0
while a < 5:
	print (a)
	a += 1

print("1) Contando de 3 a 4 usando While")
a = 3
while a < 5:
	print (a)
	a += 1

print("1) Contando de 0 a 4 usando For")
for a in range(5):
	print (a)

print("1) Contando de 3 a 4 usando For")
for a in range(3,5):
	print (a)



print("2) Iterando um lista usando While")
a = 0
vetor = [10,20,30,40,50]
while a < len(vetor):
	print( vetor[a] )
	a += 1

print("2) Iterando um lista usando For")
vetor = [10,20,30,40,50]
for i in range( len(vetor) ):
	print(i)



print("3) Iterando um dicionario usando For")
vetor = {"name": "felipe", "score": 10, "age": 27}
for key,val in vetor.items() :
	print(key,val)
