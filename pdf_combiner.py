# PyPDF2
# COMBINER

# lire des PDF extraire le texte

""" Ecrire des PDF
  - Combiner 
  - Rotation, superposer
  - Ne peut pas : rajouter du texte ou des images """
from PyPDF2 import PdfWriter, PdfReader

contenu_sortie = PdfWriter()

fichier_pdf_presentation = open("presentation.pdf", "rb")
fichier_pdf_recap = open("recap.pdf", "rb")

reader_presentation = PdfReader(fichier_pdf_presentation)
reader_recap = PdfReader(fichier_pdf_recap)

print("Nombre de pages du fichier récap : ", len(reader_recap.pages))

contenu_sortie.add_page(reader_presentation.pages[0])
for i in range(len(reader_recap.pages)):
    contenu_sortie.add_page(reader_recap.pages[i])


fichier_sortie = open("fichier_sortie.pdf", "wb")
contenu_sortie.write(fichier_sortie)

fichier_pdf_presentation.close()
fichier_pdf_recap.close()
fichier_sortie.close()
