from Classe_Relatorio import Relatorio
from Classe_dataset import CDataSet



d = CDataSet()

class Menu:
    relatorio = Relatorio(d)

    def submenu_graficos_linha(self):
        while True:
            print("\n--- GRÁFICOS DE LINHA ---")
            print("1 Evolução da expectativa de vida por país")
            print("2 Evolução global da expectativa de vida por ano")
            print("3 Comparar expectativa de vida entre dois países")
            print("0. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                d.expectativa_por_pais()
            elif opcao == '2':
                d.expectativa_ao_longo_dos_anos()
            elif opcao == '3':
                d.comparar_paises()
            elif opcao == '0':
                break
            else:
                print("Opção inválida.")

    def submenu_barras(self):
        while True:
            print("\n--- GRÁFICOS DE BARRAS ---")
            print("1 Top 10 países com maior escolaridade por ano")
            print("2 Top 10 países com maior expectativa de vida por ano")
            print("3 Gasto em saúde por país em um ano")
            print("0. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                d.escolaridade_por_ano()
            elif opcao == '2':
                d.top_paises_barras()
            elif opcao == '3':
                d.gasto_saude_ano()
            elif opcao == '0':
                break
            else:
                print("Opção inválida.")
    
    def submenu_pizza(self):
        while True:
            print("\n--- GRÁFICOS DE PIZZA ---")
            print("1 Proporção de países por status (desenvolvido vs. em desenvolvimento)")
            print("2 Distribuição por faixa de expectativa de vida (<60, 60–70, 70–80, >80)")
            print("0. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                d.grafico_pizza_status()
            elif opcao == '2':
                d.pizza_faixa_expectativa()
            elif opcao == '0':
                break
            else:
                print("Opção inválida.")

    def submenu_histogramas(self):
        while True:
            print("\n--- HISTOGRAMAS ---")
            print("1 Distribuição da escolaridade")
            print("2 Distribuição do consumo de álcool")
            print("3 Distribuição da expectativa de vida")
            print("0. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                d.histograma_escolaridade()
            elif opcao == '2':
                d.histograma_alcool()
            elif opcao == '3':
                d.histograma_vida()
            elif opcao == '0':
                break
            else:
                print("Opção inválida.")
    
    def submenu_correlacoes(self):
        while True:
            print("\n--- MAPAS DE CORRELAÇÃO ---")
            print("1 Correlação entre todas as variáveis")
            print("2 Correlação da expectativa de vida com outras variáveis")
            print("0. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                d.correlacoes()
            elif opcao == '2':
                d.correlacao_expectativa()
            elif opcao == '0':
                break
            else:
                print("Opção inválida.")

    def submenu_estatisticas(self):
        while True:
            print("\n--- ESTATÍSTICAS E TABELAS ---")
            print("1. Estatísticas descritivas do dataset")
            print("2. Países com maior e menor expectativa de vida por ano")
            print("3. País com maior gasto em saúde")
            print("4. País com maior vacinação infantil")
            print("5. Estatísticas descritivas por país")
            print("6. Média de expectativa de vida por status de desenvolvimento")
            print("7. País com maior e menor expectativa de vida média (geral)")
            print("0. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                d.estatisticas_gerais()
            elif opcao == '2':
                d.top_paises()
            elif opcao == '3':
                d.maior_gasto_saude()
            elif opcao == '4':
                d.maior_vacinacao()
            elif opcao == '5':
                d.estatisticas_por_pais()
            elif opcao == '6':
                d.media_expectativa_por_status()
            elif opcao == '7':
                d.extremos_expectativa_media()
            elif opcao == '0':
                break
            else:
                print("Opção inválida.")





