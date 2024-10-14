# SQLITE : CREATION DE LA TABLE

import sqlite3

# • connexion = "albums2.db"
# executer / curseur
# commit
# fermer

connexion = sqlite3.connect("albums2.db")

curseur = connexion.cursor()

curseur.execute(
    """CREATE TABLE artiste(
  artiste_id INTERGER NOT NULL PRIMARY KEY, 
  nom VARCHAR);"""
)

# albums
curseur.execute(
    """CREATE TABLE album(
  album_id INTERGER NOT NULL PRIMARY KEY,
  artiste_id INTEGER REFERENCES artiste, 
  titre VARCHAR,
  annee_sortie INTEGER);"""
)

# artistes -> MJ, CD
curseur.execute('INSERT INTO artiste (artiste_id, nom) VALUES (1, "Michael Jackson");')
mj_id = curseur.lastrowid

curseur.execute('INSERT INTO artiste (artiste_id, nom) VALUES (2, "Céline Dion");')
cd_id = curseur.lastrowid

# albums -> Thriller, 2x
# artist ID 1/2
curseur.execute(
    "INSERT INTO album (album_id, artiste_id, titre, annee_sortie) VALUES (1, "
    + str(mj_id)
    + ', "Thriller", 1982);'
)
curseur.execute(
    "INSERT INTO album (album_id, artiste_id, titre, annee_sortie) VALUES (2, "
    + str(cd_id)
    + ', "Falling Into You", 1996);'
)
curseur.execute(
    "INSERT INTO album (album_id, artiste_id, titre, annee_sortie) VALUES (3, "
    + str(cd_id)
    + ', "Let\'s Talk about Love", 1997);'
)


connexion.commit()
connexion.close()
