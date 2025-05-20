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
    
    def correlacoes(self):
        corr = self._df.corr(numeric_only=True)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Mapa de Correlação')
        plt.show()
    
    def top_paises(self):
        ano = int(input("Digite o ano (ex: 2013): "))
        top = self._df[self._df['Year'] == ano]
        if top.empty:
            print("Ano não encontrado.")
            return
        print("\nTop 5 Países com MAIOR expectativa de vida:")
        print(top[['Country', 'Life expectancy ']].sort_values(by='Life expectancy ', ascending=False).head())
        print("\nTop 5 Países com MENOR expectativa de vida:")
        print(top[['Country', 'Life expectancy ']].sort_values(by='Life expectancy ').head())

    def histograma_variavel(self):
        variavel = input("Digite o nome da variável (ex: Alcohol, Schooling): ")
        if variavel not in self._df.columns:
            print("Variável inválida.")
            return
        plt.figure(figsize=(8,5))
        sns.histplot(self._df[variavel].dropna(), bins=20, kde=True)
        plt.title(f'Distribuição de {variavel}')
        plt.xlabel(variavel)
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.show()