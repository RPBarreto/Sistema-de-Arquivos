import os
def renamefiledir(nome):
    path = os.getcwd()
    totalpath= os.path.join(path,nome)
    try:
        os.rename(totalpath)
    except OSError:
        print("Falha na renomeação da pasta ou arquivo" % totalpath)
    else:
        print("pasta ou arquivo renomeado com sucesso")