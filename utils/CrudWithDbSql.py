import sqlite3

con = sqlite3.connect("crud.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS TB_usuarios(usu_id INTEGER PRIMARY KEY AUTOINCREMENT, usu_nome TEXT)")

def CreateUser(usu_nome):
    cur.execute("INSERT INTO TB_usuarios (usu_nome) VALUES (?)", (usu_nome,))
    con.commit()
    print("Usuário criado!")

def Read():
    for linha in cur.execute("SELECT * FROM TB_usuarios"):
        print(linha)

def UpdateUser(usu_id, usu_nome):
    cur.execute("UPDATE TB_usuarios SET usu_nome = ? WHERE usu_id = ?", (usu_nome, usu_id))
    con.commit()
    print("Usuário atualizado!")

def RemoveUSer(usu_id):
    cur.execute("DELETE FROM TB_usuarios WHERE usu_id = ?", (usu_id,))
    con.commit()
    print("Usuário removido!")

