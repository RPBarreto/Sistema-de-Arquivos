# Sistema de Arquivos

Sistema de arquivos escrito em Python, a raiz é o diretório /root.

Commandos:
Operações sobre arquivos:

    - Criar arquivo (touch nome_arquivo)
    - Remover arquivo (rm nome_arquivo)
    - Escrever no arquivo (echo "conteudo legal" >> nome_arquivo)
    - Ler arquivo (cat nome_arquivo)
    - Copiar arquivo (cp nome_arquivo1 nome_arquivo2)
    - Renomear arquivo (mv nome_arquivo1 nome_arquivo2)
    
Operações sobre diretórios:

    - Criar diretório (mkdir nome_diretorio)
    - Remover diretório (rmdir nome-diretorio) - só funciona se diretório estiver vazio
    - Trocar de diretório (cd nome_diretorio)
        cd . e cd .. (troca diretorio)
    - Renomear diretorio (mv nome_diretorio1 nome_diretorio2)

Como usar:

Necessário Python instalado.

Rode o arquivo main.py e já estará pronto para uso.

Há persistência e os arquivos serão criados normalmente, podendo ser acessados por outros programas e exploradores de arquivos.

Problemas conhecidos:
Dependendo do sistema, ou interpretador, poderá ocorrer que o sistema reconheça os comandos como comandos nativo do seu terminal, ou seja os verdadeiros e não os implementados nestes algoritmos.

Bruno Dias 108349
Davi Ribeiro 88931
Renan Barreto 85486
