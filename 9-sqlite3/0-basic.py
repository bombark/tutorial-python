
import sqlite3


db = sqlite3.connect('projeto.db')

print("  1) inserir um item na base de dados")
cursor = db.cursor();
cursor.execute("INSERT INTO users (name,age) VALUES (?,?)", ("ssss",20) )
db.commit()


print("  2) listar todos os itens da base de dados")
cursor = db.cursor();
cursor.execute("SELECT * FROM users;")
for item in cursor.fetchall():
	print(item)
cursor.close()


print("  3) listar um item da base de dados")
cursor = db.cursor();
cursor.execute("SELECT * FROM users WHERE id=1;")
for item in cursor.fetchall():
	print(item)
cursor.close()
