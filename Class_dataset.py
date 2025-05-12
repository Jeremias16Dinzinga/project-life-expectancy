
import pandas as pd


class CDataSet:
    def __init__(self):
        self.nome_ficheiro = "ORIGINAL/Life Expectancy Data.csv"
        self.__df = pd.read_csv(
            self.nome_ficheiro, sep=","
        )

    def dimensao(self):
        return {"linhas": self.__df.shape[0],
                "colunas": self.__df.shape[1]
                }

    def info(self):
        print(self.__df.info)

    def descricao(self):
        print(self.__df.describe().to_string())

    def ver(self):
        print(self.__df)


d = CDataSet()
x = d.dimensao()

print (x)
# d.ver()
# d.info()
d.descricao()
