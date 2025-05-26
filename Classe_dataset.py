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
        df_grouped = self._df.groupby('Year')['Life expectancy '].mean()
        df_grouped.plot(title='Expectativa de vida média por ano')
        plt.ylabel('Expectativa de vida')
        plt.grid(True)
        plt.show()
    
    def comparar_paises(self):
        pais1 = input("Digite o nome do primeiro país: ")
        pais2 = input("Digite o nome do segundo país: ")
        dados = self._df[self._df['Country'].isin([pais1, pais2])]
        if dados.empty:
            print("Um ou ambos os países não foram encontrados.")
        else:
            sns.lineplot(data=dados, x='Year', y='Life expectancy ', hue='Country')
            plt.title(f'Comparação da Expectativa de Vida: {pais1} vs {pais2}')
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
    
    def top_paises_barras(self):
        ano = int(input("Digite o ano (ex: 2013): "))
        top = self._df[self._df['Year'] == ano]
        if top.empty:
            print("Ano não encontrado.")
            return

        top_maiores = top[['Country', 'Life expectancy ']].sort_values(by='Life expectancy ', ascending=False).head(5)
        top_menores = top[['Country', 'Life expectancy ']].sort_values(by='Life expectancy ').head(5)

        fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

        sns.barplot(data=top_maiores, x='Life expectancy ', y='Country', palette='Greens_r', ax=axes[0])
        axes[0].set_title(f'Top 5 MAIOR Expectativa de Vida em {ano}')
        axes[0].set_xlabel('Expectativa de Vida')
        axes[0].set_ylabel('País')
        axes[0].grid(True)

        sns.barplot(data=top_menores, x='Life expectancy ', y='Country', palette='Reds', ax=axes[1])
        axes[1].set_title(f'Top 5 MENOR Expectativa de Vida em {ano}')
        axes[1].set_xlabel('Expectativa de Vida')
        axes[1].set_ylabel('')
        axes[1].grid(True)

        plt.tight_layout()
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

    def gasto_saude_ano(self):
        ano = int(input("Digite o ano: "))
        dados = self._df[self._df['Year'] == ano]
        top10 = dados[['Country', 'percentage expenditure']].sort_values(by='percentage expenditure', ascending=False).head(10)
        sns.barplot(data=top10, x='percentage expenditure', y='Country', palette='coolwarm')
        plt.title(f'Top 10 países com maior gasto em saúde em {ano}')
        plt.xlabel('Gasto em saúde (%)')
        plt.ylabel('País')
        plt.grid(True)
        plt.show()

    def grafico_pizza_status(self):
        status_counts = self._df['Status'].value_counts()
        status_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#ff9999'])
        plt.title('Distribuição por Status de Desenvolvimento')
        plt.ylabel('')
        plt.show()

    def pizza_faixa_expectativa(self):
        bins = [0, 60, 70, 80, 100]
        labels = ['<60', '60–70', '70–80', '>80']
        self._df['Faixa'] = pd.cut(self._df['Life expectancy '], bins=bins, labels=labels)
        faixa_counts = self._df['Faixa'].value_counts().sort_index()
        faixa_counts.plot.pie(autopct='%1.1f%%', startangle=90)
        plt.title('Distribuição por Faixa de Expectativa de Vida')
        plt.ylabel('')
        plt.show()
    
    def histograma_escolaridade(self):
        plt.figure(figsize=(8,5))
        sns.histplot(self._df['Schooling'].dropna(), bins=20, kde=True)
        plt.title('Distribuição da Escolaridade')
        plt.xlabel('Anos de Escolaridade')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.show()

    def histograma_alcool(self):
        plt.figure(figsize=(8,5))
        sns.histplot(self._df['Alcohol'].dropna(), bins=20, kde=True)
        plt.title('Distribuição do Consumo de Álcool')
        plt.xlabel('Consumo de Álcool')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.show()

    def histograma_vida(self):
        plt.figure(figsize=(8,5))
        sns.histplot(self._df['Life expectancy '].dropna(), bins=20, kde=True)
        plt.title('Distribuição da Expectativa de Vida')
        plt.xlabel('Expectativa de Vida')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.show()

    def correlacoes(self):
        corr = self._df.corr(numeric_only=True)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Mapa de Correlação')
        plt.show()

    def correlacao_expectativa(self):
        corrs = self._df.corr(numeric_only=True)['Life expectancy '].sort_values(ascending=False)
        print("\nCorrelação da Expectativa de Vida com outras variáveis:")
        print(corrs)

    def maior_gasto_saude(self):
        gasto = self._df[['Country', 'Year', 'percentage expenditure']].sort_values(by='percentage expenditure', ascending=False).head(1)
        print("\nPaís com maior gasto em saúde:")
        print(gasto)

    def maior_vacinacao(self):
        vac = self._df[['Country', 'Year', 'Hepatitis B']].sort_values(by='Hepatitis B', ascending=False).head(1)
        print("\nPaís com maior vacinação infantil (Hepatite B):")
        print(vac)
