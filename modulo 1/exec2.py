candidatos = {}
votos = {}
v_branco = 0
v_nulo = 0

def menu():
    while True:
        print("="*40)
        print("1 - Cadastro de candidatos")
        print("2 - Iniciar a votação")
        print("3 - Resultado")
        print("0 - Sair")
        print("="*40)

        opcao = input(">> ")

        if opcao == "1":
            cadastro()
        elif opcao == "2":
            votacao()
        elif opcao == "3":
            analise()
        elif opcao == "0":
            break
        else:
            print("Opção inválida")

def cadastro():
    nome = input("Nome do candidato: ")
    numero = input("Número do candidato: ")

    if numero in candidatos:
        print("Número já cadastrado!")
    else:
        candidatos[numero] = nome
        votos[numero] = 0
        print(f"Candidato {nome} cadastrado com sucesso!")

def votacao():
    global v_branco, v_nulo
    print("Digite 'c' para sair da votação.\n")
    while True:
        num = input("N° do candidato: ")

        if num.lower() == "c":
            break
        elif num == "":
            v_branco += 1
            print("Voto em branco registrado!")
        elif num in candidatos:
            op = input(f"{candidatos[num]} | Confirmar voto? (S/N) ").upper()
            if op == "S":
                votos[num] += 1
                print("Voto computado!")
        else:
            v_nulo += 1
            print("Voto nulo registrado!")

def analise():
    print("\n=== RESULTADO DA VOTAÇÃO ===")
    for numero, nome in candidatos.items():
        print(f"{nome} ({numero}) - {votos[numero]} voto(s)")
    print(f"Votos em branco: {v_branco}")
    print(f"Votos nulos: {v_nulo}")
    print("="*40)

def principal():
    menu()

if __name__ == "__main__":
    principal()
