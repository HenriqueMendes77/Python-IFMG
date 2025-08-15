def calcular_aumento(salario):
    if salario <= 2000:
        return salario * 0.20
    elif salario <= 5000:
        return salario * 0.15
    else:
        return salario * 0.05

def lista_salario_baixo(funcionarios):
    print("\nFuncionários com salário menor que R$2.000,00:")
    for nome, salario_antigo, salario_novo in funcionarios:
        if salario_novo < 2000:
            print(f"- {nome}: R${salario_novo:,.2f}")

def main():
    funcionarios = []
    total_antigo = 0.0
    total_novo = 0.0

    print("Digite os dados dos funcionários. Para encerrar, digite '0' no nome.\n")

    while True:
        nome = input("\nNome: ").strip()

        if nome == "0":
            break

        try:
            salario = float(input("Salário (R$): ").replace(",", "."))
        except ValueError:
            print("Valor inválido! Digite apenas números.")
            continue

        aumento = calcular_aumento(salario)
        novo_salario = salario + aumento

        funcionarios.append((nome, salario, novo_salario))

        total_antigo += salario
        total_novo += novo_salario

    total_aumento = total_novo - total_antigo

    print("\n" + "=" * 40)
    print(f"Total de aumento: R${total_aumento:,.2f}")
    print("=" * 40)

    lista_salario_baixo(funcionarios)

if __name__ == "__main__":
    main()
