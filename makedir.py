# -*- coding: utf-8 -*-
import os
def makedir(nome):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)
    try:
        if(nome==root):
            raise Exception("Nome Invalido")
        else:
            os.mkdir(totalpath)
    except Exception as e:
        print("Erro" % e)
    except OSError:
        print("Falha na criação da pasta" % totalpath)
    else:
        print("pasta criada com sucesso")