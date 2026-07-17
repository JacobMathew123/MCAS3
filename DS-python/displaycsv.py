import pandas as pd
df=pd.read_csv("data.csv")
print("First row:")
print(df.head(1))
print("\nLast row:")
print(df.tail(1))