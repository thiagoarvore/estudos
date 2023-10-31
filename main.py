from fastapi import FastAPI, HTTPException
from modules import movie_list, find_movie, delete_movie, insert_movie, escolher_genero, deletar_genero, select_by_gender, insert_estudio, insert_genero
import sqlite3

app = FastAPI()

@app.get("/")
async def root():
    try:
        with sqlite3.connect('moviedb.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM movies")
            result = cursor.fetchall()
            cursor.close()
            db.close()
        return result        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno no servidor")

@app.post("/addestudio/")
async def add_estudio(id: int, nome: str):
    try:
        with sqlite3.connect('moviedb.db')as db:
            cursor = db.cursor()        
            cursor.execute("INSERT INTO estudios VALUES (?, ?)", (id, nome))
            db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno no servidor")
    return "estudio inserido"

@app.post("/addgender/")
async def add_gender(id: int, nome: str):
    return insert_genero(id, nome)

@app.post("/setgender/")
async def set_gender(id_movie: int, id_genero: int):
    return escolher_genero(id_movie, id_genero)

@app.post("/addmovie/")
async def add_movie(id: int, titulo: str, release: int, id_estudio: int):
    return insert_movie(id, titulo, release, id_estudio)

@app.get("/find_movie/{movie_id}")
async def findmovie(movie_id: int):
    {"movie_id": movie_id}
    return find_movie(movie_id)

@app.get("/selectbygender/{gender_id}")
async def selectbygender(gender_id: int):
    {"gender_id": gender_id}
    return select_by_gender(gender_id)

