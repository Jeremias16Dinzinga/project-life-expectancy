import pandas as pd

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
