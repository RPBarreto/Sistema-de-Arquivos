# Sistema de Arquivos

Sistema de arquivos escrito em Python, a raiz é o diretório /root.

Commandos:
Operações sobre arquivos:

    - Criar arquivo (touch arquivo)
    - Remover arquivo (rm arquivo)
    - Escrever no arquivo (echo "conteudo legal" >> arquivo)
    - Ler arquivo (cat arquivo)
    - Copiar arquivo (cp arquivo1 arquivo2)
    - Renomear arquivo (mv arquivo1 arquivo2)
    
Operações sobre diretórios:

    - Criar diretório (mkdir diretorio)
    - Remover diretório (rmdir diretorio) - só funciona se diretório estiver vazio
    - Trocar de diretório (cd diretorio)
        * Não esquecer dos arquivos especiais . e .. 
    - Renomear diretorio (mv diretorio1 diretorio2)

Como usar:
Necessário Python instalado.
Rode o arquivo main.py e já estará pronto para uso.
Há persistência e os arquivos serão criados normalmente, podendo ser acessados por outros programas e exploradores de arquivos.

Problemas conhecidos:
Dependendo do sistema, ou interpretador, poderá ocorrer que o sistema reconheça os comandos como comandos nativo do seu terminal, ou seja os verdadeiros e não os implementados nestes algoritmos.
