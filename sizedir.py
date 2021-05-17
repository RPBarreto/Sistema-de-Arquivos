import os


def sizedir(path):
    path = os.getcwd()
    size = 0
    for filename in os.listdir(path):
        size += os.path.getsize(os.path.join(path, filename))
    print('Tamanho do diretorio ' + str(size) + ' bytes')
    return size
