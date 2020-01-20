import pandas as pd

Web = {"Day": [1, 2, 3, 4],
       "Visitors": [100, 90, 80, 40],
       "Bounce_Rate": [20, 20, 25, 15]}

df = pd.DataFrame(Web)
print(df.head(1))
print(df.tail(1))
