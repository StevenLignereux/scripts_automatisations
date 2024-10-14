# SQLITE : lecture de la table
import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

# curseur.execute("SELECT * FROM artiste")
""" curseur.execute("SELECT nom FROM artiste")
artistes = curseur.fetchall()
print(artistes) """

""" for artiste in curseur.execute("SELECT * FROM artiste"):
    print(artiste) """

""" for artiste in artistes:
    print(artiste[1]) """

album_cd = curseur.execute(
    'SELECT titre FROM album a JOIN artiste ar ON a.artiste_id = ar.artiste_id AND ar.nom = "Céline Dion"'
).fetchall()
print(album_cd)


curseur.close()
