

print ("   1.1) Definindo uma classe chamado Pessoa")
class Pessoa:
	name = ""
	age = 0
	cpf = ""


	def __init__(self,name):
		self.name = name
		print("criando objeto Pessoa {}".format(self.name))

	def __del__(self):
		print("destruindo o objeto Pessoa {}".format(self.name))

	def calcula(self,a,b):
		return a + b;

	def pensa_uma_frase(self):
		raise BaseException("Funcao nao implementada!")

	def __str__(self):
		return "name: {}, idade: {}, cpf: {}".format(
			self.name, self.age, self.cpf
		)



print ("   1.2) Criando um objeto do tipo Pessoa")
pedrao = Pessoa("pedro")

print ("   1.3) Lendo um atributo da pessoa pedrao")
print(pedrao.name)

print ("   1.4) Alterando um atributo da pessoa pedrao")
print(pedrao.name)
pedrao.name = "felipe"
print(pedrao.name)

print ("   1.5) Chamando um metodo da pessoa pedrao")
res = pedrao.calcula(20,30)
print(res)

print("   1.6) Facilitando o print de um objeto usando o metodo __str__")
print(pedrao)





print ("\n\n\n   2.1) Definindo uma subclasse Usuario")
class Usuario(Pessoa):
	email = ""
	password = ""

	def __init__(self,name):
		print("criando objeto Usuario {}".format(self.name))

	def __del__(self):
		print("destruindo o objeto Usuario {}".format(self.name))

	def login(self,password):
		return self.password == password


print ("   2.2) Criando um objeto do tipo Usuario")
user = Usuario("joao")

print ("   2.3) Lendo um atributo do usuario user")
print(user.name)

print ("   2.4) Alterando um atributo do usuario user")
print(user.name)
user.name = "felipe"
print(user.name)

print ("   2.5) Chamando o metodo calcula do usuario user")
user.calcula(20,30)

print("   1.6) Facilitando o print de um objeto usando o metodo __str__")
print(user)
