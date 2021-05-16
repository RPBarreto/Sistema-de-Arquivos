import os
def removefile(nome):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)
    if os.path.exists(totalpath):
        os.remove(totalpath)
    else:
        print("Arquivo não Existe")