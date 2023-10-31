import sqlite3

#criação do banco de dados
# db = sqlite3.connect('moviedb.db')
# cursor = db.cursor()

#criação de tabelas
# # cursor.execute("""CREATE TABLE generos (
#                id integer Primary Key, 
#                nome text Not Null)""")
# cursor.execute("""CREATE TABLE estudios (
#                id integer Primary Key, 
#                nome text Not Null)""")
# cursor.execute("""CREATE TABLE movies (
#                id integer Primary Key, 
#                titulo text Not Null, 
#                release integer Not Null,                
#                id_estudio integer,
#                FOREIGN KEY(id_estudio) references estudios (id) ON DELETE SET NULL)""")
# cursor.execute("""CREATE TABLE users (
#                id integer Primary Key, 
#                nome text Not Null, 
#                email text Not Null, 
#                senha text Not Null, 
#                date DATETIME Not Null)""")
# cursor.execute("""CREATE TABLE tabela1 (
#                id_movie integer Not Null,
#                id_genero integer Not Null,
#                Foreign Key (id_genero) references generos (id) ON DELETE SET NULL,
#                Foreign Key (id_movie) references movies (id) ON DELETE SET NULL)""")
# cursor.execute("""CREATE TABLE reviews (
#                id integer Primary Key, 
#                id_movie integer Not Null,
#                id_user integer Not Null,
#                date datetime Not Null, 
#                rating integer Not Null,
#                sinopse text Not Null,
#                Foreign Key (id_user) references users (id) ON DELETE SET NULL,
#                Foreign Key (id_movie) references movies (id) ON DELETE SET NULL)""")

#funções
def insert_movie(id, titulo, release, id_estudio):
    try:
        with sqlite3.connect('moviedb.db') as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO movies (id, titulo, release, id_estudio) VALUES (?, ?, ?, ?)", (id, titulo, release, id_estudio))
        print("Filme inserido com sucesso.")
    except sqlite3.Error as e:
        print("Erro ao inserir filme:", e)

def delete_movie(id):
    try:
        with sqlite3.connect('moviedb.db') as db:
            cursor = db.cursor()        
            cursor.execute("DELETE FROM movies WHERE id = ?", (id))
        db.commit()
    except Exception as e:
        print("Erro:", e)   
        return None

def insert_genero(id, nome):
    try:
        with sqlite3.connect('moviedb.db')as db:
            cursor = db.cursor()        
            cursor.execute("INSERT INTO generos VALUES (?, ?)", (id, nome))
            db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print("Erro:", e)   
        return None

def insert_estudio(id, nome):
    try:
        with sqlite3.connect('moviedb.db')as db:
            cursor = db.cursor()        
            cursor.execute("INSERT INTO estudios VALUES (?, ?)", (id, nome))
            db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print("Erro:", e)   
        return None

def escolher_genero(id_movie, id_genero):
    db = sqlite3.connect('moviedb.db')
    cursor = db.cursor()        
    cursor.execute("INSERT INTO tabela1 VALUES ("+int(id_movie)+", "+int(id_genero)+")")
    db.commit()
    cursor.close()
    db.close()

def deletar_estudio(id):
    try: 
        db = sqlite3.connect('moviedb.db')
        cursor = db.cursor()        
        cursor.execute("DELETE FROM estudios WHERE  id=(?)", (id))
        db.commit()
        db.close()
    except Exception as e:
        print("Erro:", e)   
        return None

def deletar_genero(id):
    try:    
        db = sqlite3.connect('moviedb.db')
        cursor = db.cursor()        
        cursor.execute("DELETE FROM generos WHERE  id=?)(?)", (id))
        db.commit()
        db.close()
    except Exception as e:
        print("Erro:", e)   
        return None

def movie_list():
    try:
        with sqlite3.connect('moviedb.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM movies")
            result = cursor.fetchall()
            cursor.close()
            db.close()
        return result        
    except Exception as e:
        print("Erro:", e)   
        return None

def find_movie(titulo):
    try:
        db = sqlite3.connect('moviedb.db')
        cursor = db.cursor()
        cursor.execute("SELECT id FROM movies WHERE titulo = ?", (titulo,))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result        
    except Exception as e:
        print("Erro:", e)   
        return None

def select_by_gender(id_genero):
    try:
        db = sqlite3.connect('moviedb.db')
        cursor = db.cursor()
        cursor.execute("SELECT "+id_genero+" FROM tabela1")
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result        
    except Exception as e:
        print("Erro:", e)   
        return None

def select_by_studio(id_estudio):
    try:
        db = sqlite3.connect('moviedb.db')
        cursor = db.cursor()
        cursor.execute("SELECT "+id_estudio+" FROM movies")
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result        
    except Exception as e:
        print("Erro:", e)   
        return None

  
        