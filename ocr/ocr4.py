from pypdfocr import pypdfocr
import multiprocessing
from multiprocessing import forking
from pypdfocr import pypdfocr_multiprocessing
from pypdfocr_multiprocessing import _Popen
forking.Popen = _Popen

multiprocessing.freeze_support()
script = pypdfocr.PyPDFOCR()
arguments = [pypdfocr, "Sabrina_parte_1_2.pdf"]
script.go(arguments[1:])
