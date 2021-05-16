import appendfile
import changedir
import copyfile
import createfile
import deletedir
import makedir
import readfile
import removefile
import renamefiledir


def tratamento(input):
    comando = raw_input()
    comandoRaw = comando
    comando.split()
    comandoRaw.split("")  # nao funciona

    if (comando[0] == "SHUTDOWN"):
        break
    if (comando[0] == "touch"):
        createfile(comando[1])
        comando = []
    if (comando[0] == "rm"):
        removefile(comando[1])
    if (comando[0] == "echo"):
    # malditas aspas
    if (comando[0] == "cat"):
        readfile(comando[1])
    if (comando[0] == "cp"):
        copyfile(comando[1], comando[2])
    if (comando[0] == "mv"):
        renamefiledir

    if (comando[0] == "mkdir"):
    if (comando[0] == "rmdir"):
    if (comando[0] == "cd"):
    if (comando[0] == "."):
    if (comando[0] == ".."):
