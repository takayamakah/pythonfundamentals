def calcula_gorjeta(valor_subtotal):
    valor_gorjeta = valor_subtotal * 0.1
    valor_total = valor_subtotal + valor_gorjeta

    detalhes_conta = []
    detalhes_conta.append(str(round(valor_subtotal, 2))) #valor_subtotal
    detalhes_conta.append(str(round(valor_gorjeta, 2))) #valor_gorjeta
    detalhes_conta.append(str(round(valor_total,2))) #valor_total

    return detalhes_conta

def main():
    valor_subtotal = float(input("Qual o valor total da conta? ").replace(",", "."))

    detalhes_conta = []
    detalhes_conta = calcula_gorjeta(valor_subtotal)

    print(f"Valor Total da Conta: {detalhes_conta[0]}")
    print(f"Valor da Gorjeta (10%): {detalhes_conta[1]}")
    print(f"Valor Total a Pagar: {detalhes_conta[2]}")


if __name__ == "__main__":
    main()