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
    c.execute('''CREATE TABLE IF NOT EXISTS post (name text, author text, desc text)''')


    # Save (commit) the changes
    conn.commit()
    c.close()

def insert_post(post_name,author_name,descripcion):

     # open connection and cursor
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = dict_factory
    c = conn.cursor()    

    # Insert a row of data
    c.execute("INSERT INTO post VALUES ('%s','%s','%s')" % (post_name,author_name,descripcion))
    

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
    c.execute("SELECT * from post")
    posts = c.fetchall() 


    return posts
    c.close()
