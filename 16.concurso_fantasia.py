#Questão 03 da TP3 de Lógica, Computação e Algoritmos
#Algoritimo que verifica quem é o vencedor a partir de informações adquiridas em tela
#Obs: Este algoritimo não tem tratamento para notas iguais

import os

def get_vencedor(participantes, notas):
    #verifica o maior número em uma lista
    maior_nota = max(notas)

    #procura o participante pela nota
    participante = participantes[notas.index(maior_nota)]
    
    #cria variável do tipo lista com os dados do partipante vencedor
    vencedor = [participante, maior_nota]

    return  vencedor


def main():
    #Iniciando variáveis de lista
    participantes = []
    notas = []

    #Captura quantidade de particantes que estão concorrendo no concurso
    npart = int(input("\nQuantos participantes estão concorrendo? "))
    
    #Repete a captura de dados dos partipantes em relação ao número informado anteriormente
    for i in range(npart):
        #Captura o nome do participante
        participante = input(f"\nQual o Nome do Participante {i+1}: ")
        
        #Enquanto os dados forem inválidos, a captura da nota se repete
        dados_validos = False
        while not dados_validos:
            try:                
                #Captura nota do participante na tela
                nota = float(input(f"Qual a NOTA do Participante {i+1}: ").replace(",","."))
                
                #Se nota dentro do intervalo entre 0 e 10, inclui dados nas listas e seta dados como válidos
                if nota >= 0 and nota <= 10:
                    participantes.append(participante)
                    notas.append(nota)               
                    dados_validos = True
                else:
                    #Se nota inválida, mostra mensagem de alerta em tela e repete o processo
                    print("\nNota deve estar entre 0 e 10!")
            except:
                #Se erro, mostra mensagem de erro em tela
                print("\nDados inválidos!")

    #Chama função que verifica quem foi o vencedor entre as informações recolhidas
    vencedor = get_vencedor(participantes, notas)

    #Imprime em tela o vencedor e sua pontuação
    print(f"\n\nA pessoa vencedora é {vencedor[0]} com {vencedor[1]} pontos!")    


if __name__ == "__main__":
    #Limpa a tela
    os.system('cls')

    #Imprime em tela título do algoritimo
    print("Concurso de Fantasias\n")
    
    #Chama a função principal
    main()

    #Imprime em tela finalização do algoritimo
    print("\nEnd\n")