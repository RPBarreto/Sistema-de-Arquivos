# Sistema de Arquivos
 
Operações sobre arquivos:

    - Criar arquivo (touch arquivo) - Função Feita(create)
    - Remover arquivo (rm arquivo) - Função Feita(removefile)
    - Escrever no arquivo (echo "conteudo legal" >> arquivo) - Feito(appendfile)
    - Ler arquivo (cat arquivo) - Feito (readfile)
    - Copiar arquivo (cp arquivo1 arquivo2) - Função feita (copyfile)
    - Renomear arquivo (mv arquivo1 arquivo2) - Função Feita (renamefiledir)

Operações sobre diretórios:

    - Criar diretório (mkdir diretorio) - Função Feita (makedir)
    - Remover diretório (rmdir diretorio) - só funciona se diretório estiver vazio - Função Feita (deletedir)
    - Trocar de diretório (cd diretorio) - Feito (changedir)
        * Não esquecer dos arquivos especiais . e .. 
    - Renomear diretorio (mv diretorio1 diretorio2) - Função Feita (renamefiledir)

TODO: 

    - Main - Done
    - Tratamento de string de comando para todas funções - Done
    - Verificar Root na troca de diretório - Done
    - i-nodes:
    - Criação do i-node principal
    - criação do i-node por arquivo
    - Metodos que precisam de verificação com inodes: touch, rm, echo, cp, mv, mkdir, rmdir

