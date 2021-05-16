from filesize import filesize
import os
def createinodefile(nome):
    path = os.getcwd()
    
    totalpath= os.path.join(path,nome)
    nome = 'inode' + nome #+ 'txt'
    totalpath2= os.path.join(path,nome)

    if os.path.exists(totalpath2):
        print("Inode já Existe")
    else:
        f=open(totalpath2,"w")
        print("Inode criado")
        f.write(totalpath+'\n')
        f.write(str(filesize(totalpath))+'\n')
        #loop e verificar pra ver quantos blocos pega
        f.close