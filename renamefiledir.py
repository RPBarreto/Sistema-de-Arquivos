# -*- coding: utf-8 -*-
import os
def renamefiledir(nome,alvo):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)
    totalpath2 = os.path.join(path,alvo)
    try:
        os.rename(totalpath,totalpath2)
    except OSError:
        print("Falha na renomeação da pasta ou arquivo" % totalpath)
    else:
        print("pasta ou arquivo renomeado com sucesso")