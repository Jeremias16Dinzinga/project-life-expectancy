import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CDataSet:
    def __init__(self):
        self.nome_ficheiro = "ORIGINAL/Life Expectancy Data.csv"
        self._df = pd.read_csv(
            self.nome_ficheiro, sep=","
        )

    def estatisticas_gerais(self):
        print("\nResumo Estatístico:")
        print(self._df.describe())
        print("\nInformações:")
        print(self._df.info())
    
    def expectativa_por_pais(self):
        pais = input("Digite o nome do país: ")
        dados_pais = self._df[self._df['Country'] == pais]
        if dados_pais.empty:
            print("País não encontrado.")
        else:
            dados_pais.plot(x='Year', y='Life expectancy ', title=f'Expectativa de Vida - {pais}')
            plt.ylabel('Expectativa de vida')
            plt.grid(True)
            plt.show()

    def expectativa_ao_longo_dos_anos(self):
        self._df_grouped = self._df.groupby('Year')['Life expectancy '].mean()
        self._df_grouped.plot(title='Expectativa de vida média por ano')
        plt.ylabel('Expectativa de vida')
        plt.grid(True)
        plt.show()

    def comparacao_status(self):
        sns.boxplot(x='Status', y='Life expectancy ', data=self._df)
        plt.title('Comparação: Desenvolvido vs. Em Desenvolvimento')
        plt.ylabel('Expectativa de vida')
        plt.show()