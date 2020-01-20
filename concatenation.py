import pandas as pd

Web1 = {"Day": [1, 2, 3, 4],
        "Visitors": [100, 90, 80, 40],
        "Bounce_Rate": [20, 20, 25, 15]}

Web2 = {"Month": [1, 2, 3, 4],
        "Users": [100, 90, 80, 40],
        "Bounce_Rate_Plus": [20, 20, 25, 15]}

df1 = pd.DataFrame(Web1, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame(Web2, index=[2004, 2006, 2007, 2008])

Concat = pd.concat([df1, df2])
print(Concat)
