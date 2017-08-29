from pypdfocr import pypdfocr
import multiprocessing
from multiprocessing import forking
from pypdfocr import pypdfocr_multiprocessing
import sys, os, multiprocessing.forking
import logging

""" Special work-around to support multiprocessing and pyinstaller --onefile on windows systms
    https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Multiprocessing
"""

import multiprocessing.forking as forking
import os
import sys

class _Popen(multiprocessing.forking.Popen):
    def __init__(self, *args, **kw):
        if hasattr(sys, 'frozen'):
            # We have to set original _MEIPASS2 value from sys._MEIPASS
            # to get --onefile mode working.
            os.putenv('_MEIPASS2', sys._MEIPASS)
        try:
            super(_Popen, self).__init__(*args, **kw)
        finally:
            if hasattr(sys, 'frozen'):
                # On some platforms (e.g. AIX) 'os.unsetenv()' is not
                # available. In those cases we cannot delete the variable
                # but only set it to the empty string. The bootloader
                # can handle this case.
                if hasattr(os, 'unsetenv'):
                    os.unsetenv('_MEIPASS2')
                else:
                    os.putenv('_MEIPASS2', '')

forking.Popen = _Popen


multiprocessing.freeze_support()
script = pypdfocr.PyPDFOCR()
arguments = [pypdfocr, "Sabrina_parte_1_2.pdf"]
script.go(arguments[1:])
