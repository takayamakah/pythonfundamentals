def calcula_area_retangulo(altura, base):
    return round(altura * base, 2)

def main():
    print("Calcular área de um retângulo \n")
    
    altura = float(input("Qual o comprimento da altura do retângulo (m)? ").replace(",", "."))
    base = float(input("Qual o comprimento da base do retângulo (m)? ").replace(",", "."))

    print(f"\nÁrea do retângulo: {calcula_area_retangulo(altura, base)} m² \n")


if __name__ == "__main__":
    main()