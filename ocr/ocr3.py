#Codigo que recebe um pdf, transforma em um pdf pesquisavel, extrai o texto de cada pagina do
#documento e guarda em uma lista

#Utiliza o pacote pypdfocr
#Necessario instalar:
##pypdfocr - https://pypi.python.org/pypi/pypdfocr
##Tesseract OCR software https://code.google.com/p/tesseract-ocr/
##GhostScript http://www.ghostscript.com/
##ImageMagick http://www.imagemagick.org/
##Poppler http://poppler.freedesktop.org/

#Tambem utiliza o pacote slate
#Necessario instalar:
##slate
##pdfminer
##pdfdocuments

import subprocess
import slate

def pdfocr(document):
	command1 = "pypdfocr -l por "
	command = command1+document  
	subprocess.call(command)
	#add2name = ocr

def gettext(document):
	doc = slate.PDF(document)
	return doc

documentname = "Sabrina_parte_1_2.pdf"
documentname2 = "Sabrina_parte_1_2_ocr.pdf"

pdfocr(documentname)
doc = gettext(documentname2)

print doc