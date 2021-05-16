from typing import Text
import appendfile
import changedir
import copyfile
import createfile
import deletedir
import makedir
import readfile
import removefile
import renamefiledir
import re

def tratamento(input):
    comando = input
    comandoRaw = comando
    comando.split()
    comandoRaw.split("")  # nao funciona

    if (comando[0] == "SHUTDOWN"):
        return(True)
    if (comando[0] == "touch"):
        createfile(comando[1])
    if (comando[0] == "rm"):
        removefile(comando[1])
    if (comando[0] == "echo"):
        text = re.search('"(.*)"', input)
        appendfile(comando[-1],text)
    # malditas aspas
    if (comando[0] == "cat"):
        readfile(comando[1])
    if (comando[0] == "cp"):
        copyfile(comando[1], comando[2])
    if (comando[0] == "mv"):
        renamefiledir(comando[1])
    if (comando[0] == "mkdir"):
        makedir(comando[1])
    if (comando[0] == "rmdir"):
        deletedir(comando[1])
    if (comando[0] == "cd"):
        changedir(comando[1])
    if (comando[0] == "."):
        changedir(comando[1])
    if (comando[0] == ".."):
        changedir(comando[1])
