# FICHIER TEXTE : EXERCICE
# "Ecrire des nombres"

# nombres.txt
# 1
# 2
# 3
# for
# 10 lignes

f = open("nombres.txt", "w")

for i in range(10):
    f.write(str(i+1)+"\n")

f.close()