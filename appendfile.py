# -*- coding: utf-8 -*-
import os
def appendfile(nome,conteudo):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)

    if os.path.exists(totalpath):
        f=open(totalpath,"a")
        f.write(conteudo)
        f.close

    else:
        print("Arquivo não encontrado")
