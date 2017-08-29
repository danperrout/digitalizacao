# Funcao que converte uma imagem em pdf em um arquivo txt
from PIL import Image as Image2
from wand.image import Image
import pyocr
import pyocr.builders
import io

def pdf2txt(arquivo):

    tools = pyocr.get_available_tools()

    tool = tools[0]

    print("Will use tool '%s'" % (tool.get_name()))

    langs = tool.get_available_languages()

    print("Available languages: %s" % ", ".join(langs))

    lang = langs[1]

    print("Will use lang '%s'" % (lang))

    req_image = []
    final_text = []

    image_pdf = Image(filename="relatorio.pdf", resolution=300)
    image_jpeg = image_pdf.convert('jpeg')

    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))

    for img in req_image:
        txt = tool.image_to_string(
            Image2.open(io.BytesIO(img)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)

    return final_text;

teste = "relatorio.pdf"
final_text = pdf2txt(teste)
