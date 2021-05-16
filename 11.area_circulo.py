import math

def calcula_area_circulo(raio):
    return round(math.pi*(raio**2), 2)

def main():
    print("Calcular área de um círculo \n")
    
    raio = float(input("Qual o comprimento do raio do círculo (m)? ").replace(",", "."))

    print(f"\nÁrea do círculo: {calcula_area_circulo(raio)} m² \n")


if __name__ == "__main__":
    main()