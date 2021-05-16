import math

def calcula_volume_cilindro(raio, altura):
    return round(math.pi*(raio**2)*altura, 2)

def main():
    print("Calcular área de uma caixa d'água cilíndrica \n")
    
    raio = float(input("Qual o comprimento do raio da caixa d'agua (m)? ").replace(",", "."))
    altura = float(input("Qual o comprimento da altura da caixa d'agua (m)? ").replace(",", "."))

    print(f"\nÁrea da caida d'água: {calcula_volume_cilindro(raio, altura)} m³ \n")


if __name__ == "__main__":
    main()