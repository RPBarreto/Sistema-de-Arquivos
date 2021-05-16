import os
def renamefiledir(nome):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)
    try:
        os.chdir(totalpath)
    except OSError:
        print("arquivo não encontrado" % totalpath)
    else:
        print("arquivo encontrado")