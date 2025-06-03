
from Menus import *
m = Menu()

def menu_principal():
    while True:
        print("\n========= MENU PRINCIPAL =========")
        print("1. Gráficos de Linha")
        print("2. Gráficos de Barras")
        print("3. Gráficos de Pizza")
        print("4. Histogramas")
        print("5. Mapas de Correlação")
        print("6. Estatísticas e Tabelas")
        print("7. Gerar relatório Word")
        print("8. Converter relatório para PDF")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            m.submenu_graficos_linha()
        elif opcao == '2':
            m.submenu_barras()
        elif opcao == '3':
            m.submenu_pizza()
        elif opcao == '4':
            m.submenu_histogramas()
        elif opcao == '5':
            m.submenu_correlacoes()
        elif opcao == '6':
            m.submenu_estatisticas()
        elif opcao == '7':            
            m.relatorio.gerar_word()
        elif opcao == '8':
             m.relatorio.converter_para_pdf()            
        elif opcao == '9':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()


