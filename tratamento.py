# -*- coding: utf-8 -*-
from typing import Text
from appendfile import *
from changedir import *
from copyfile import *
from createfile import *
from deletedir import *
from makedir import *
from readfile import *
from removefile import *
from renamefiledir import *


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
        appendfile(comando[-1], text)
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
