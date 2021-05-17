from filesize import filesize
import os


def createinodefile(nome):
    path = os.getcwd()
    print(path)
    print(nome)
    totalpath = os.path.join(path, nome)
    nome = 'inode' + nome  # + 'txt'
    totalpath2 = os.path.join(path, nome)

    if os.path.exists(totalpath2):
        print("Inode já Existe")
    else:
        f = open(totalpath2, "w")
        print("Inode criado")
        blocks = (int(filesize(totalpath)/4096)) + \
            (filesize(totalpath) % 4096 > 0)
        print("Tamanho do arquivo " + str(filesize(totalpath)))
        print("Blocos ocupados " + str(blocks))
        f.writelines([(totalpath+'\n'), (str(blocks) + '\n')])
        f.write(str(os.stat(totalpath))+'\n')
        f.close
