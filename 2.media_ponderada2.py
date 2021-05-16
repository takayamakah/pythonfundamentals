def listar(valores):
    lista = []
    posi = 0
    valor = 0.0
    validador = False
    ult_valor = False
    
    while not validador:               
        if not ult_valor:
            posf = valores.find(",")        
            valor = (valores[posi:posf])
            valores = valores[posf+1:]
        else:
            valor = valores

        lista.append(float(valor))     
        
        if ult_valor:
            validador = True
        elif valores.find(",") < 0 and not ult_valor:
            ult_valor = True
        
    return lista

def calcula_media_ponderada(lista_notas, lista_pesos):  
    nota_peso = 0.0
    soma_peso = 0.0

    for i in range(len(lista_notas)):
        nota_peso = nota_peso + lista_notas[i]*lista_pesos[i]
        soma_peso = soma_peso + lista_pesos[i]
    
    return str(round(nota_peso/soma_peso, 2))


if __name__ == "__main__":
    calcular = True
    while calcular:
        aluno = input("Nome Aluno(a): ")
        
        validador = False
        while not validador: 
            notas = input("Digite as notas separadas por vírgula: ")
            pesos = input("Digite os pesos separados por vírgula: ")

            if notas.find(",") > 0 and pesos.find(",") > 0:
                lista_notas = listar(notas)
                lista_pesos = listar(pesos)

                validador = True
            else:
                print("Digite mais de uma nota e peso!")

        media_ponderada = calcula_media_ponderada(lista_notas, lista_pesos)
        print(f"A média ponderada de {aluno} é: {media_ponderada}")

        if not input("Deseja calcular mais notas? (s/n)  ") == "s":
            calcular = False
