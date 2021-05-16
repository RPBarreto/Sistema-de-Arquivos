# -*- coding: utf-8 -*-
import os
def makedir(nome):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)
    try:
        os.mkdir(totalpath)
    except OSError:
        print("Falha na criação da pasta" % totalpath)
    else:
        print("pasta criada com sucesso")