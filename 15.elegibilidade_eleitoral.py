#Questão 02 da TP3 de Lógica, Computação e Algoritmos
#Verificar a elegibilidade eleitoral a partir de uma idade

import os

def imprime_instrucoes():
    print("ATENÇÃO - Instruções ao final da mensagem")
    print("1) Para verificar mais idades aperte 2 vezes ENTER.")
    print("2) Para sair do sistema aperte SPACE e ENTER.\n")

def elegibilidade(idade):
    if idade >= 18 and idade < 70:
        return "\nEleitor Obrigatório" 
    elif (idade >= 16 and idade < 18) or (idade >= 70):
        return "\nEleitor facultativo" 
    elif idade < 16:
        return "\nNão tem direito a voto"


def main():    
    continuar = True
    while continuar:
        try:
            idade_valida = False
            while not idade_valida:
                #Captura idade em tela
                idade = int(input("\nIdade: "))

                if idade > 0:
                    idade_valida = True
                else:
                    print("\nIdade deve ser maior que zero!")
        except:
            print("\nIdade inválida!")

        print(elegibilidade(idade))

        if input() == " ":
            continuar = False



if __name__ == "__main__":
    #Limpa a tela
    os.system('cls')

    #Imprime em tela título do algoritimo
    print("Verificar a elegibilidade eleitoral a partir de uma idade\n")
    
    #Imprime em tela instruções para utilização do algoritimo
    imprime_instrucoes()

    #Chama a função principal
    main()

    #Imprime em tela finalização do algoritimo
    print("\nEnd")