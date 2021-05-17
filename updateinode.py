from filesize import filesize
import os


def updateinodefile(nome):
    path = os.getcwd()

    totalpath = os.path.join(path, nome)
    nome = 'inode' + nome  # + 'txt'
    totalpath2 = os.path.join(path, nome)

    if os.path.exists(totalpath2):

        f = (open(totalpath2, "w"))
        f.writelines([(totalpath+'\n'),(str(filesize(totalpath)) + '\n')])
        print("Inode Atualizado")
        f.close
    else:

        print("Inode não Existe")


        # loop e verificar pra ver quantos blocos pega