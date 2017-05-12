import sqlite3

#donde se guardara la base de datos sqlite
conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()

def create_db():

    cursor.execute("""CREATE TABLE IF NOT EXISTS post
                  (title text, artist text, release_date text, 
                   publisher text, media_type text) 
               """)
    conn.commit()
def insert_db():

    #insertar una linea de datos
    cursor.execute("INSERT INTO post VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")
    cursor.execute("INSERT INTO post VALUES ('Noticias','Ortega Y Gasset','2/2/2000','Anon','Text')")
    # save data to database
    conn.commit()



def consulta_all_post():
    #consultar los datos de la tabla post
    return cursor.execute("SELECT * FROM post")
consulta_all_post()