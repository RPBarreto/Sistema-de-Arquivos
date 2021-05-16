# -*- coding: utf-8 -*-
import os
def deletedir(nome):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)
    try:
        os.rmdir(totalpath)
    except OSError:
        print("Falha em deletar a pasta" % totalpath)
    else:
        print("pasta deletada com sucesso")