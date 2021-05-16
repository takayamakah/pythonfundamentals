def calcula_area_quadrado(lado):
    return round(lado**2, 2)

def main():
    print("Calcular área de um quadrado \n")
    
    lado = float(input("Qual o comprimento do lado do quadrado (m)? ").replace(",", "."))

    print(f"\nÁrea do quadrado: {calcula_area_quadrado(lado)} m² \n")


if __name__ == "__main__":
    main()