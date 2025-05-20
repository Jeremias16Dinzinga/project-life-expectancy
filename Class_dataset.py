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
    
    def grafico_pizza_status(self):
        status_counts = self._df['Status'].value_counts()
        status_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#ff9999'])
        plt.title('Distribuição por Status de Desenvolvimento')
        plt.ylabel('')
        plt.show()

    def comparar_paises(self):
        pais1 = input("Digite o nome do primeiro país: ")
        pais2 = input("Digite o nome do segundo país: ")
        df1 = self._df[self._df['Country'] == pais1]
        df2 = self._df[self._df['Country'] == pais2]
        if df1.empty or df2.empty:
            print("Um ou ambos os países não foram encontrados.")
            return
        plt.plot(df1['Year'], df1['Life expectancy '], label=pais1)
        plt.plot(df2['Year'], df2['Life expectancy '], label=pais2)
        plt.title('Comparação de Expectativa de Vida')
        plt.xlabel('Ano')
        plt.ylabel('Expectativa de vida')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def escolaridade_por_ano(self):
        ano = int(input("Digite o ano: "))
        dados = self._df[self._df['Year'] == ano]
        top10 = dados[['Country', 'Schooling']].sort_values(by='Schooling', ascending=False).head(10)
        sns.barplot(data=top10, x='Schooling', y='Country', palette='viridis')
        plt.title(f'Top 10 países com maior escolaridade em {ano}')
        plt.xlabel('Anos de Escolaridade')
        plt.ylabel('País')
        plt.grid(True)
        plt.show()
