import os
def createfile(nome):
    if os.path.exists(nome):
        print("Arquivo não Existe")
    else:
        f=open(nome,"x")
        print("Arquivo criado")
