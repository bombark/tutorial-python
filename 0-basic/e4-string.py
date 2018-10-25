
print("\n1) Concatecao de string")
w1 = "this"
w2 = "is"
w3 = "sparta"
f1 = w1+w2+w3
print(f1)
print(w1+w2+w3)


print("\n2) Formatacao de string")
w1 = "this"
w2 = "is"
w3 = "sparta!!"
f2 = "frase: {} {} {}!!!".format(w1,w2,w3)
print(f2)


print("\n3) substitui todos os 'and' por 'or'")
raw = "this is a phrase with visis"
texto = raw.replace("is","are")
print(texto)



raw = """
	The village church is dedicated to St James the Great and was built on land
	donated by the Earl of Shrewsbury and largely paid for by him. It has a
	large circular stained glass east window, an unusually tall south porch
	and an open stone bell turret mounted at the east end of the church hung
	with two bells. The impressive wood rood screen was designed by Augustus
	Pugin. The village lies less than a mile to the north of Hopton Heath,
	which was a significant battlefield (Battle of Hopton Heath) in the English
	Civil War where in 1643 Parliamentarian forces were defeated by Royalists
	under Spencer Compton, who died there.
"""



print("\n4) divide a string em vetor usando como separador a string ' '")
words = raw.split(' ')
print(words)


print("\n5) divide a string em vetor usando como separador a string ' '")
phrases = raw.split('.')
print(phrases)
