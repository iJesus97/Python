import sqlite3
miConexion = sqlite3.connect("BaseSitioRamaIEEE.db")
miCursor = miConexion.cursor()
#miCursor.execute("CREATE TABLE CAROUSELINDEX (ID INTEGER PRIMARY KEY AUTOINCREMENT, CAROUSELTITLE VARCHAR(50), CAROUSELPARAGRAPH VARCHAR(100), CAROUSELBUTTON VARCHAR(20))")
miCursor.execute("""CREATE TABLE INDEXPOSTS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    POSTTITLE VARCHAR(50), 
    POSTDATE VARCHAR(100), 
    POSTAUTHOR VARCHAR(20)
    )""")
miConexion.commit()

miConexion.close()