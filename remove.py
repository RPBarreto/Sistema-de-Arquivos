import os
def remove(nome):
    if os.path.exists(nome):
        os.remove(nome)
    else:
        print("Arquivo não Existe")