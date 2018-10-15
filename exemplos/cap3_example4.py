f=float(input("informe a média[0.0 a 10.0]: "))
if f >= 7.0:
	if f>=9.0:
		print("Parabéns Nerd")
	else:
		print("Aprovado")
elif f <7.0 and f >= 5.0:
	print("Recuperação")
else:
	print("Reprovado")
