from filesize import filesize
import os


def updateinodefile(nome):
    path = os.getcwd()

    totalpath = os.path.join(path, nome)
    nome = 'inode' + nome  # + 'txt'
    totalpath2 = os.path.join(path, nome)

    if os.path.exists(totalpath2):

        f = (open(totalpath2, "w"))
        blocks = (int(filesize(totalpath)/4096)) + \
            (filesize(totalpath) % 4096 > 0)
        f.writelines([(totalpath+'\n'), (str(blocks) + '\n')])
        f.write(str(os.stat(totalpath))+'\n')
        print("Inode Atualizado")
        print("Tamanho do arquivo " + str(filesize(totalpath)))
        print("Blocos ocupados " + str(blocks))
        f.close
    else:

        print("Inode não Existe")

        # loop e verificar pra ver quantos blocos pega
