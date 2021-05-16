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
import re


def tratamento(input):
    comando = input
    comandoRaw = comando
    command = comando.split()
    comandoRaw.split("")  # nao funciona

    if (comando[0] == 'SHUTDOWN'):
        return(True)
    if (comando[0] == 'touch'):
        createfile(command[1])
    if (comando[0] == 'rm'):
        removefile(command[1])
    if (comando[0] == 'echo'):
        text = re.search('"(.*)"', input)
        appendfile(command[-1], text)
    # malditas aspas
    if (comando[0] == 'cat'):
        readfile(command[1])
    if (comando[0] == 'cp'):
        copyfile(command[1], command[2])
    if (comando[0] == 'mv'):
        renamefiledir(command[1])
    if (comando[0] == 'mkdir'):
        makedir(command[1])
    if (comando[0] == 'rmdir'):
        deletedir(command[1])
    if (comando[0] == 'cd'):
        changedir(command[1])
    if (comando[0] == '.'):
        changedir(command[1])
    if (comando[0] == '..'):
        changedir(command[1])
