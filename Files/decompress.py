from zipfile import *

f=ZipFile('imag.zip','r')
f.extractall()
f.close()