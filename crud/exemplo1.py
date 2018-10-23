#=================================  HEADER  ====================================

import sqlite3
import copy
import getpass

import hashlib
from hashlib import md5

#-------------------------------------------------------------------------------



#================================  DATABASE  ===================================

class Database:
	table_map = {}

	def __init__(self):
		self.table_map["users"] = UserPkg();

	def table(self,name):
		return self.table_map[name];

#-------------------------------------------------------------------------------



#=================================  TABLES  ====================================

class Table:
	def all(self):
		raise BaseException("nao implementado")

	def find(self,id):
		raise BaseException("nao implementado")

	def insert(self,model):
		raise BaseException("nao implementado")


class UserPkg(Table):
	data=[]

	def all(self):
		return self.data

	def find(self,id):
		return self.data[id];

	def insert(self,user):
		user.id = len(self.data)
		copia = copy.copy(user)
		self.data.append( copia )

	def make(self):
		return User(self)

#-------------------------------------------------------------------------------


#=================================  MODELS =====================================

class User:
	id = -1

	def __init__(self,table,email="",name=""):
		self.table = table
		self.email = email
		self.name  = name

	def save(self):
		self.table.insert(self)

	def __str__(self):
		return 'email: {}, name: {};'.format(self.email,self.name)



#-------------------------------------------------------------------------------



#==================================  MAIN  =====================================

def calc_md5(texto):
	maq = hashlib.md5()
	maq.update(texto.encode('utf-8'))
	return maq.digest()



def cadastrar_usuario(db):
	print("--- PUT /users/new ---")
	raise BaseException("implementar funcao")
	# verificar se email contem @
	print("usuario cadastrado com sucesso!\n")

def listar_usuarios(db):
	print("--- GET /users/ ---")
	raise BaseException("implementar funcao")
	print("")

def pesquisar_usuario(db):
	print("--- GET /users/? ---")
	raise BaseException("implementar funcao")
	print("")

def apagar_usuarios(db):
	print("--- DEL /users/1 ---")
	raise BaseException("implementar funcao")
	print("")



def sign_in():
	pass
	#raise("implementar funcao")



def main():
	sign_in()
	db = Database();
	opcoes = {
		"1": cadastrar_usuario,
		"2": listar_usuarios,
		"3": pesquisar_usuario,
		"4": apagar_usuarios
	}

	while True:
		print("--- GET / ---")
		print("  1) cadastrar usuario")
		print("  2) listar usuarios")
		print("  3) pesquisar usuario")
		print("  4) apagar usuario")
		print("")
		opt = input()

		try:
			func = opcoes.get(opt, lambda: "Invalid month")
			func(db)
		except Exception as e:
			print("error: "+str(e))


#-------------------------------------------------------------------------------



#================================  __INIT__  ===================================

print("Iniciando Projeto")
main()

#-------------------------------------------------------------------------------
