from docx import Document
from docx.shared import Inches
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')
from fpdf import FPDF

class Relatorio:
    def __init__(self, dataset):
        self.dataset = dataset
        self.df_filtrado = dataset._df.copy()
    
    def filtrar_por_pais(self, pais):
        self.df_filtrado = self.dataset._df[self.dataset._df["Country"] == pais]
        if self.df_filtrado.empty:
            print("País não encontrado.")
        else:
            print(f"{len(self.df_filtrado)} registros encontrados para {pais}.")

    def gerar_word(self, nome_arquivo="Relatorio.docx"):
        doc = Document()
        doc.add_heading('Relatório Completo de Expectativa de Vida', 0)
                
        doc.add_heading("1. Estatísticas Descritivas", level=1)
        stat = self.df_filtrado.describe().round(2).to_string()
        doc.add_paragraph(stat)
        
        doc.add_heading("2. Top 5 Países com Maior e Menor Expectativa de Vida", level=1)
        for ano in [2013, 2015]:
            doc.add_heading(f"Ano: {ano}", level=2)
            dados_ano = self.df_filtrado[self.df_filtrado["Year"] == ano]
            if dados_ano.empty:
                doc.add_paragraph("Sem dados para este ano.")
                continue

            maiores = dados_ano[['Country', 'Life expectancy ']].sort_values(by='Life expectancy ', ascending=False).head(5)
            menores = dados_ano[['Country', 'Life expectancy ']].sort_values(by='Life expectancy ').head(5)

            doc.add_paragraph("Top 5 - Maior expectativa de vida:")
            doc.add_paragraph(maiores.to_string(index=False))

            doc.add_paragraph("Top 5 - Menor expectativa de vida:")
            doc.add_paragraph(menores.to_string(index=False))
        
        doc.add_heading("3. País com Maior Gasto em Saúde", level=1)
        gasto = self.df_filtrado.groupby('Country')["Total expenditure"].mean().sort_values(ascending=False).head(1)
        doc.add_paragraph(gasto.to_string())
        
        doc.add_heading("4. País com Maior Vacinação Infantil", level=1)
        vac = self.df_filtrado.groupby('Country')["percentage expenditure"].mean().sort_values(ascending=False).head(1)
        doc.add_paragraph(vac.to_string())
        
        doc.add_heading("5. Gráfico de Expectativa de Vida por Ano", level=1)
        grafico_path = "grafico_linha.png"
        self.df_filtrado.groupby("Year")["Life expectancy "].mean().plot(title="Evolução da Expectativa de Vida")
        plt.ylabel("Expectativa de Vida")
        plt.savefig(grafico_path)
        plt.close()
        doc.add_picture(grafico_path, width=Inches(5))
        os.remove(grafico_path)
        
        doc.add_heading("6. Gráfico de Gasto em Saúde por Ano", level=1)
        grafico_path2 = "grafico_gasto.png"
        self.df_filtrado.groupby("Year")["Total expenditure"].mean().plot(kind='bar', title="Gasto em Saúde Médio por Ano")
        plt.ylabel("Gasto em Saúde")
        plt.tight_layout()
        plt.savefig(grafico_path2)
        plt.close()
        doc.add_picture(grafico_path2, width=Inches(5))
        os.remove(grafico_path2)

        doc.add_heading("7. Gráfico de Pizza: Status dos Países", level=1)
        grafico_path3 = "grafico_pizza.png"
        self.df_filtrado["Status"].value_counts().plot.pie(autopct='%1.1f%%', title="Distribuição por Status")
        plt.ylabel('')
        plt.savefig(grafico_path3)
        plt.close()
        doc.add_picture(grafico_path3, width=Inches(4))
        os.remove(grafico_path3)

        doc.add_heading("8. Conclusão", level=1)
        doc.add_paragraph("Este relatório apresenta um panorama completo sobre os dados de expectativa de vida, "
                        "com destaque para os países com melhores indicadores, variações anuais e estatísticas relevantes.")

        doc.save(nome_arquivo)
        print(f"Relatório Word gerado: {nome_arquivo}")

    
    def converter_para_pdf(self, doc_path="relatorio.docx", pdf_path="relatorio.pdf"):
        from docx2pdf import convert
        convert(doc_path, pdf_path)
        print(f"Relatório PDF gerado: {pdf_path}")
