import pandas as pd

Web1 = {"Day": [1, 2, 3, 4],
        "Visitors": [100, 90, 80, 40],
        "Bounce_Rate": [20, 20, 25, 15]}

df1 = pd.DataFrame(Web1, index=[2001, 2002, 2003, 2004])

df1.set_index("Day", inplace=True)
df1 = df1.rename(columns = {"Visitors":"Users"})
print(df1)