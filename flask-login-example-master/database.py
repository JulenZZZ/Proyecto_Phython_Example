import sqlite3


#donde se guardara la base de datos sqlite
conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def create_db():
    # open connection and cursor
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = dict_factory
    c = conn.cursor()    
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS posts (name text, author text, desc text, img text)''')


    # Save (commit) the changes
    conn.commit()
    c.close()

def insert_post(post_name,author_name,descripcion,imagen):

     # open connection and cursor
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = dict_factory
    c = conn.cursor()    

    # Insert a row of data
    c.execute("INSERT INTO posts VALUES ('%s','%s','%s','%s') order by post_name desc" % (post_name,author_name,descripcion,imagen))
    

    # Save (commit) the changes
    conn.commit()
    c.close()



def consulta_all_post():
    #consultar los datos de la tabla post
       # open connection and cursor
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = dict_factory
    c = conn.cursor()    

    # select all students
    c.execute("SELECT * from posts")
    posts = c.fetchall() 


    return posts
    c.close()

def delete_post(name_borrar):
    #consultar los datos de la tabla post
    # open connection and cursor
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = dict_factory
    c = conn.cursor()

    #borrar post 
    sql="DELETE  FROM posts WHERE name ="+name_borrar
    c.execute(sql)

    #commit
    conn.commit()
    c.close()
def search_post(name_buscar):
    #abrir conexion y cursor
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = dict_factory
    c = conn.cursor()

    #buscar post
    sql= "SELECT * FROM posts WHERE name LIKE "+"'%"+name_buscar+"%'" 
    c.execute(sql)
    posts = c.fetchall() 
    c.close()
    
    return posts

   
    
