from filesize import filesize
import os
def createinodefile(nome):
    path = os.getcwd()
    print(path)
    print(nome)
    totalpath= os.path.join(path,nome)
    nome = 'inode' + nome #+ 'txt'
    totalpath2= os.path.join(path,nome)

    if os.path.exists(totalpath2):
        print("Inode já Existe")
    else:
        f=open(totalpath2,"w")
        print("Inode criado")
        f.write(totalpath+'\n')
        print (totalpath2)
        f.write(str(filesize(totalpath))+'\n')
        #loop e verificar pra ver quantos blocos pega
        f.close