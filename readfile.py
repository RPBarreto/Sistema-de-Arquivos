import os
def readfile(nome):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)

    if os.path.exists(totalpath):
        f=open(totalpath,"r")
        print(f.read())
        f.close

    else:
        print("Arquivo não encontrado")
