#=================================  HEADER  ====================================

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
		raise("nao implementado")

	def find(self,id):
		raise("nao implementado")

	def insert(self,model):
		raise("nao implementado")


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

	def __str__(self):
		return 'email: {}, name: {};'.format(self.email,self.name)

	def save(self):
		self.table.insert(self)

#-------------------------------------------------------------------------------



#==================================  MAIN  =====================================


def cadastrar_usuario(db):
	print("--- PUT /users/new ---")

	while True:
		email = input("email: ");
		if email.find("@") < 0:
			print("infome um email valido")
		else:
			break

	name = input("name: ");
	user = db.table("users").make()
	user.name = name
	user.email = email
	user.save()
	print("usuario cadastrado com sucesso!\n")


def listar_usuarios(db):
	print("--- GET /users/ ---")
	userpkg = db.table("users").all()
	if ( len(userpkg) == 0 ):
		print("nenhum usuario cadastrado")
	else:
		for i in range( len(userpkg) ):
			print( userpkg[i] )
	print("")


def calc_md5(texto):
	maq = hashlib.md5()
	maq.update(texto.encode('utf-8'))
	return maq.digest()


def sign_in():
	while True:
		login = input("login: ")
		passwd = getpass.getpass("passwd: ")
		passwd = calc_md5(passwd)
		if login == "root" and passwd == b'\x14\xd7w\xfe\xbbq\xc560\xe9\xe8C\xbe\xdb\xd4\xd8':
			break;


def main():
	sign_in()
	db = Database();
	opcoes = {
		"1": cadastrar_usuario,
		"2": listar_usuarios
	}

	while True:
		print("--- GET / ---")
		print("  1) cadastrar usuario")
		print("  2) listar usuarios")
		print("")
		opt = input()

		func = opcoes.get(opt, lambda: "Invalid month")
		func(db)


#-------------------------------------------------------------------------------



#================================  __INIT__  ===================================

print("Iniciando Projeto")
main()

#-------------------------------------------------------------------------------
