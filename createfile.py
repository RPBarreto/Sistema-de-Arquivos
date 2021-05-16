import os
def createfile(nome):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)

    if os.path.exists(totalpath):
        print("Arquivo não Existe")
    else:
        f=open(totalpath,"x")
        print("Arquivo criado")
