
from Class_dataset import *

d = CDataSet()

def menu():
    while True:
        print("\n===== MENU DE ANÁLISE =====")
        print("1. Estatísticas gerais")
        print("2. Expectativa de vida por país")
        print("3. Expectativa de vida ao longo dos anos")
        print("4. Comparar países desenvolvidos vs. em desenvolvimento")
        print("5. Mostrar correlação entre variáveis")
        print("6. Países com maior/menor expectativa de vida em um ano")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            d.estatisticas_gerais()
        elif opcao == '2':
            d.expectativa_por_pais()
        elif opcao == '3':            
            d.expectativa_ao_longo_dos_anos()
        elif opcao == '4':            
            d.comparacao_status()
        elif opcao == '5':
            print("Processando...")
            #correlacoes()
        elif opcao == '6':
            print("Processando...")
            #top_paises()
        elif opcao == '7':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()


