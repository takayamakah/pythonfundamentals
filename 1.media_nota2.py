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

def calcula_media(lista_notas):  
    media = sum(lista_notas)/len(lista_notas)    
    return str(round(media, 2))


if __name__ == "__main__":
    calcular = True
    while calcular:
        aluno = input("Nome Aluno(a): ")
        
        validador = False
        while not validador: 
            notas = input("Digite as notas separadas por vírgula: ")

            if notas.find(",") > 0:
                lista_notas = listar(notas)
                validador = True
            else:
                print("Digite mais de uma nota e peso!")

        media = calcula_media(lista_notas)
        print(f"A média de {aluno} é: {media}")

        if not input("Deseja calcular mais notas? (s/n)  ") == "s":
            calcular = False
