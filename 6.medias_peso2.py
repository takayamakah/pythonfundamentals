def calcula_media(nota1, nota2):
    media_nota = round(((nota1 + nota2*2)/3),2)
    return str(media_nota)

def main():
    nota1 = float(input("Digite a 1ª Nota: ").replace(",", "."))
    nota2 = float(input("Digite a 2ª Nota: ").replace(",", "."))

    print("A média das suas notas é: " + calcula_media(nota1, nota2))


if __name__ == "__main__":
    main()