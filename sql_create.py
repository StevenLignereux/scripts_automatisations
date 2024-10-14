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


connexion.commit()
connexion.close()
