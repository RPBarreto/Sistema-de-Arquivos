# -*- coding: utf-8 -*-
import os
def appendfile(nome,conteudo):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)

    if os.path.exists(totalpath):
        f=open(totalpath,"a")
        f.write(conteudo)
        f.close
        print("Sucesso")
    else:
        print("Arquivo não encontrado")
