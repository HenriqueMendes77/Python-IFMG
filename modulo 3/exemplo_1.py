print('Informe os dados de cada contato para gravação')
print('Deixe em branco para parar')
arq = open('contatos.txt', 'w')
while True:
    contato = input('Contato: ')
    if contato == '':
        break
    arq.write(contato + '\n')
arq.close()
