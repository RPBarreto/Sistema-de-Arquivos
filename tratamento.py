newLine = raw_input()
newLineRaw = newLine
newLine.split()
newLineRaw.split("")  # nao funciona

if (newLine[0] == "SHUTDOWN")
    break
if (newLine[0] == "touch")
    createfile(newLine[1])
    newLine = []
if (newLine[0] == "rm")
    removefile(newLine[1])
if (newLine[0] == "echo")
# malditas aspas
if (newLine[0] == "cat")
    readfile(newLine[1])
if (newLine[0] == "cp")
    copyfile(newLine[1], newLine[2])
if (newLine[0] == "mv")
    renamefiledir

if (newLine[0] == "mkdir")
if (newLine[0] == "rmdir")
if (newLine[0] == "cd")
if (newLine[0] == ".")
if (newLine[0] == "..")
