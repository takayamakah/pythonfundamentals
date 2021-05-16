import math

def calcula_area_esfera(raio):
    return round((4*math.pi)*(raio**2), 2)

def main():
    print("Calcular área de uma esfera \n")
    
    raio = float(input("Qual o comprimento do raio da esfera (m)? ").replace(",", "."))

    print(f"\nÁrea da esfera: {calcula_area_esfera(raio)} m² \n")


if __name__ == "__main__":
    main()