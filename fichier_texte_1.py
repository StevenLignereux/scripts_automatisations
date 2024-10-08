# FICHIERS
#
# ouvrir (open) <- nom du fichier
# ecrire (write) / lire (read)
#fermer (close)
#

f = open("mon_fichier.txt", "w")


# f.write("Bonjour\n")
# f.write("Bonjour")
l = ["premiere phrase", "deuxieme phrase", "troiseme phrase"]

f.writelines("\n".join(l))
f.write("\nFin")

f.close
