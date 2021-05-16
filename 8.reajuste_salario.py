def calcula_reajuste_salario(salario):
    reajuste = salario * 0.073
    novo_salario = salario + reajuste

    detalhes_salario = []
    detalhes_salario.append(str(round(salario, 2))) #salario
    detalhes_salario.append(str(round(reajuste, 2))) #reajuste
    detalhes_salario.append(str(round(novo_salario, 2))) #novo_salario

    return detalhes_salario

def main():
    salario = float(input("Qual o valor do salário? ").replace(",", "."))

    detalhes_salario = []
    detalhes_salario = calcula_reajuste_salario(salario)

    print(f"Salário: {detalhes_salario[0]}")
    print(f"Reajuste (7,3%): {detalhes_salario[1]}")
    print(f"Novo Salário: {detalhes_salario[2]}")


if __name__ == "__main__":
    main()