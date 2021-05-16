def conversao_temp(temp, tipo_conv):
    temp_conv = []

    if tipo_conv == "C":
        temp_conv.append((temp-32) * 5/9)
        temp_conv.append("°C")
    elif tipo_conv == "F":
        temp_conv.append((temp * 9/5)+32)
        temp_conv.append("°F")
        
    return temp_conv

def main():
    print("Sistema de Conversão de Temperatura (Celcius / Fahrenheit)")

    continuar = True
    validador = False

    while continuar:

        while not validador:
            tipo_conv = str(input("Digite o tipo de conversão: Para Celcius ou Fahrenheit? (c/f)  ")).upper()
        
            if tipo_conv == "C" or tipo_conv == "F":
                conv = "°F" if (tipo_conv == "C") else "°C"
                validador = True 

        temp = float(input(f"Digite a temperatura em {conv}: "))

        temp_conv = []
        temp_conv = conversao_temp(temp, tipo_conv)

        print(f"Temperatura convertida: {temp_conv[0]} {temp_conv[1]}")        

        continuar = (str(input("Deseja continuar a converter temperaturas? ")).upper() == "S")
        validador = not continuar

if __name__ == "__main__":
    main()