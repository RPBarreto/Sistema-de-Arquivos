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
from createinode import *
import re


def tratamento(input):

    command = input.split()

    if (len(command) <2 ):
        return ()
    if (command[0] == 'SHUTDOWN'):
        return(True)

    if (command[0] == 'touch'):
        createfile(command[1])
        createinodefile(command[1])
    if (command[0] == 'rm'):
        removefile(command[1])
    if (command[0] == 'echo'):
        text = re.findall(r'"([^"]*)"', input)
        appendfile(command[-1], text[0])
    if (command[0] == 'cat'):
        readfile(command[1])
    if (command[0] == 'cp'):
        if (len(command) == 3):
            copyfile(command[1], command[2])


    if (command[0] == 'mv'):
        if (len(command) == 3):
            renamefiledir(command[1],command[2])

    if (command[0] == 'mkdir'):
        makedir(command[1])
    if (command[0] == 'rmdir'):
        deletedir(command[1])
    if (command[0] == 'cd'):
        changedir(command[1])
    if (command[0] == '.'):
        changedir(command[1])
    if (command[0] == '..'):
        changedir(command[1])
