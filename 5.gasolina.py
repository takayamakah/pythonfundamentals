def calcula_litros_gasolina(valor_litro, valor_total):
    return str(round(valor_total/valor_litro,2))

def main():
    valor_litro = float((input("Digite o valor do litro da gasolina: ").replace(",", ".")))
    valor_total = float((input("Digite o valor total a pagar: ").replace(",", ".")))
    
    litros_total = calcula_litros_gasolina(valor_litro, valor_total)

    print(f" Foi abastecido [{litros_total}] litros de gasolina! \n Muito obrigado pela preferência!")


if __name__ == "__main__":
    main()

