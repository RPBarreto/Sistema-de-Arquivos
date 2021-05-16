import os
def changedir(nome):
    path = os.getcwd()
    #totalpath= os.path.join(path,nome)
    try:
        os.chdir(nome)
    except OSError:
        print("arquivo não encontrado")
    else:
        print("arquivo encontrado")