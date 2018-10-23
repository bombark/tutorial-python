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
		self.conn = sqlite3.connect('projeto.db')
		self.table_map["users"] = UserTable(self);

	def table(self,name):
		return self.table_map[name];

	def cursor(self):
		return self.conn.cursor()

	def commit(self):
		self.conn.commit()

#-------------------------------------------------------------------------------



#=================================  TABLES  ====================================

class Table:
	def __init__(self,db):
		self.db = db

	def all(self):
		out = []
		print("opa")
		cursor = self.db.cursor()
		cursor.execute("SELECT * FROM users;")
		for linha in cursor.fetchall():
			out.append( linha)
		cursor.close()
		return out

	def find(self,id):
		cursor = self.db.cursor()
		cursor.execute("SELECT * FROM users WHERE id=?;" , (id) )
		out = cursor.fetchall()
		cursor.close()
		return out[0]

	def insert(self,model):
		raise("nao implementado")


class UserTable(Table):
	def insert(self,user):
		cursor = self.db.cursor()
		cursor.execute(
			"INSERT INTO users (email,name) VALUES (?,?);" ,
			(user.email, user.name)
		)
		self.db.commit()
		cursor.close()

	def all(self):
		out = []
		list = Table.all(self)
		for user_raw in list:
			out.append( User(user_raw) )
		return out

	def make(self, raw=()):
		return User(self, raw)

#-------------------------------------------------------------------------------






#=================================  MODELS =====================================

class User:
	id = -1

	def __init__( self, table, raw=() ):
		self.table = table
		if "email" in raw:
			self.email = raw["email"]
		if "name" in raw:
			self.name = raw["name"]

	def save(self):
		self.table.insert(self)

	def __str__(self):
		return 'email: {}'.format(self.email)



#-------------------------------------------------------------------------------



#==================================  MAIN  =====================================

def calc_md5(texto):
	maq = hashlib.md5()
	maq.update(texto.encode('utf-8'))
	return maq.digest()



def cadastrar_usuario(db):
	print("--- PUT /users/new ---")

	novo = db.table("users").make();
	novo.name = "felipe"
	novo.email = "ssss"
	novo.save()

	print("usuario cadastrado com sucesso!\n")

def listar_usuarios(db):
	print("--- GET /users/ ---")

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


	while True:
		print("--- GET / ---")
		print("  1) cadastrar usuario")
		print("  2) listar usuarios")
		print("  3) pesquisar usuario")
		print("  4) apagar usuario")
		print("")

		try:
			opt = int( input() )
			if opt == 1:
				cadastrar_usuario(db)
			elif opt == 2:
				listar_usuarios(db)
			else:
				print("error")

		except Exception as e:
			print("error: "+str(e))






#-------------------------------------------------------------------------------



#================================  __INIT__  ===================================

print("Iniciando Projeto")
main()

#-------------------------------------------------------------------------------
