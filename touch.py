import os
def Touch(nome):
    if os.path.exists(nome):
        print("Arquivo não Existe")
    else:
        f=open(nome,"x")
