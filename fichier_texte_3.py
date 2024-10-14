# FICHIERS
#
# ouvrir (open) <- nom du fichier
# ecrire (write) / lire (read)
# fermer (close)
#
import os.path


filename = "mon_fichier.txt"
if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename, "r")
    texte = f.read()
    print(texte)
    f.close()
else:
    print("Le fichier n'existe pas")

"""
try:
    f = open("mon_fichiersssssss.txt", "r")
except FileNotFoundError:
    print("ERREUR : Le fichier n'a pas pu être ouvert, car il n'a pas été trouvé")
else:
    texte = f.read()
    print(texte)
    f.close()
"""
