try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

#import PythonMagick

#img = PythonMagick.Image()
#img.density("300")
#img.read("relatorio.PDF") # read in at 300 dpi
#img.write("relatorio.PNG")

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR'


print(pytesseract.image_to_string(Image.open('texto_teste.png'), lang='por'))