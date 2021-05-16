# -*- coding: utf-8 -*-
import os
import shutil

def copyfile(nome,alvo):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)
    totalpath2= os.path.join(path,alvo)
    try:
        shutil.copy(totalpath,totalpath2)
    except IOError as error:
        print("Falha na copia do arquivo" % error)
    else:
        print("arquivo copiado com sucesso")