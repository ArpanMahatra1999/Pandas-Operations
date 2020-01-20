import pandas as pd

Unemployment = pd.read_csv("C:\\Users\\Arpan Mahatra\\PycharmProjects\\Demos\\Unemployment 2008.csv", index_col=0)
Unemployment.to_html('Unemployed08.html')
