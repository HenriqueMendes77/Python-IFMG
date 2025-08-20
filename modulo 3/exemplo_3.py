import os
if not os.path.isfile('contatos.txt'):
    print('Arquivo não encontrado')
else:
    print('Contatos cadastrados:')
    arq = open('contatos.txt')
    linhas = arq.readlines()
    for contato in linhas:
        print(contato.strip())
    arq.close()
