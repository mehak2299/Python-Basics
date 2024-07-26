from zipfile import *

f=ZipFile('imag.zip','w',ZIP_DEFLATED)
f.write('dragon.jpg')
# f.write('D:\BackendDevelopment\Python Basics\Photos\dragon.jpg')
f.close()

