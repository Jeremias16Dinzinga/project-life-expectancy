# 📊 Projeto de Expectativa de Vida

Este projeto realiza análises exploratórias e gera relatórios automáticos sobre dados de expectativa de vida mundial. Utiliza Python com bibliotecas como **Pandas**, **Matplotlib**, **python-docx** e **FPDF** para processar os dados, gerar gráficos e produzir relatórios em Word e PDF.

## 🧠 Funcionalidades

### 🔍 Análise de Dados

- Cálculo dos Top 5 países com maior e menor expectativa de vida por ano
- Expectativa de vida média por ano
- País com maior gasto em saúde
- País com maior vacinação infantil
- Gráficos dinâmicos e personalizáveis

### 📊 Geração de Gráficos

- Gráficos de barras dos Top 5 países
- Gráficos de linha da evolução da expectativa de vida e de gastos
- Gráficos de pizza com distribuição por status dos países
- Histogramas da expectativa de vida

### 📝 Geração de Relatórios

- Geração automática de relatórios em formato `.docx` com os resultados da análise
- Inserção automática de gráficos nos relatórios
- Conversão dos relatórios `.docx` para `.pdf`

## 🧰 Tecnologias

- Python 3.x
- Pandas
- Matplotlib
- python-docx
- fpdf
- docx2pdf

## 🚀 Como usar

1. Instale os requisitos:
   ```bash
   pip install pandas matplotlib python-docx fpdf docx2pdf
   ```

2. Execute o programa principal:
   ```bash
   python Programa_Principal.py
   ```

3. O relatório será gerado como `Relatorio.docx` e `Relatorio.pdf`.

## 📁 Dataset

Utiliza o dataset **Life Expectancy** da [Kaggle](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who).

---

Desenvolvido por **Jeremias Dinzinga**
