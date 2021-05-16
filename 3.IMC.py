def calcula_imc(massa, altura):
    imc = round(massa / (altura ** 2), 2)
    return str(imc)


if __name__ == "__main__":
    massa = float(input('Digite a Massa em (Kg): '))
    altura = float(input('Digite a Altura em (m): '))
    print("O seu IMC é: " + calcula_imc(massa, altura))
