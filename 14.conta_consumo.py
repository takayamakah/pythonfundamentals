#Questão 01 da TP3 de Lógica, Computação e Algoritmos
#Conta de Consumo com Taxa de Serviço de resturante ou bar
 
import os
from math import floor

#Função que calcula conta total em detalhes
def calcula_conta_total(valor_conta, qtde_pessoas, taxa_servico):
    #Calcula Valor Taxa Serviço
    valor_taxa_servico = round(valor_conta * taxa_servico /100, 2)

    #Calcula Valor Total da Conta (Com valor da taxa incluído)
    valor_total_conta = round(valor_conta + valor_taxa_servico, 2)

    #Calcula Valor Total por Pessoa 
    valor_conta_pessoa = round(valor_total_conta / qtde_pessoas, 2)

    #Inclui Valores em lista 
    conta = []
    conta.append(str(valor_total_conta).replace(".",","))
    conta.append(str(valor_conta_pessoa).replace(".",","))
    conta.append(str(valor_taxa_servico).replace(".",","))

    #Retorna Valores em Lista
    return conta   

def main():
    calcula = True
    while calcula:
        #Validador se valores de entrada estão corretos.
        #Se não, repete processo de captura de tela
        validador = False
        while not validador:
            try:
                #Captura valor em telas de Valor Conta, Qtde. Pessoas a dividir e Taxa de Serviço (0 a 100)
                valor_conta  = float(input("Qual o valor da conta: R$ ").replace(",",".").replace(" ",""))
                qtde_pessoas = int(input("Dividir a conta em quantas pessoas? ").replace(" ", ""))
                taxa_servico = float(((input("Qual a Taxa de Serviço a cobrar? (de 0 a 100 %) ").replace(",",".")).replace("%","")).replace(" ",""))

                #Valida Valor da Conta
                if valor_conta <= 0:
                    print("Valor da Conta deve ser maior que 0! \n")
                #Valida Quantidade de Pessoas
                elif qtde_pessoas <= 0:
                    print("Quantidade de Pessoas deve ser maior que 0! \n")
                #Valida Taxa de Serviço
                elif taxa_servico < 0 or taxa_servico > 100:
                    print("Taxa de Serviço fora do intervalo! \n")
                #Se todos valores válidos calcula total da conta em detalhes 
                else:
                    conta = calcula_conta_total(valor_conta, qtde_pessoas, taxa_servico)    
                    
                    #Imprime os detalhes da conta
                    print("\n")
                    print(f"Valor Total da Conta: R$ {conta[0]}")
                    print(f"Valor da Conta por pessoa: R$ {conta[1]}")
                    print(f"Valor da Taxa de Serviço: R$ {conta[2]}")

                    validador = True
            except:
                #Se valores digitados inválidos, mostra mensagem em tela e captura novamente os dados
                print("Valores Inválidos! Digite novamente.. \n")

        #Questiona se usuário deseja calcular mais uma conta. Se não, termina algoritimo
        if not input("\nDeseja calcular mais uma conta? (s/n) ").upper() == "S":
            calcula = False



if __name__ == "__main__":
    #Limpa a tela
    os.system('cls')

    #Imprime em tela título do algoritimo
    print("Bares e Restaurantes - Cálculo de Contas de Consumo\n")
    
    #Chama a função principal
    main()

    #Imprime em tela finalização do algoritimo
    print("\nEnd")