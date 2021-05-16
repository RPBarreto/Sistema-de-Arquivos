# -*- coding: utf-8 -*-
import os
def changedir(nome):
    path = os.getcwd()
    root = 'root'
    last = path.split('\\')
    print(last)
    print(path)
    try:
        if (len(nome) >= 2):
            if(nome[0] == '.' and nome[1]=='.' and len(nome)<3 and last[-1]!=root):
                os.chdir(nome)
            elif(nome[0] != '.' and nome[1]!='.'):
                os.chdir(nome)
            else:
                raise Exception("raiz")
        elif(nome[0] == '.'):
                print(path)
        else:
            os.chdir(nome)
            
    except Exception as e:
        print("Erro:" % e)
    except OSError:
        print("arquivo não encontrado")
    else:
        print("arquivo encontrado")