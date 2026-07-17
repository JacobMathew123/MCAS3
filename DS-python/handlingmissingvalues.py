import pandas as pd
import numpy as np
data={"Name":["Alice",np.nan,"Charlie","David",np.nan],
      "Age":[25,30,np.nan,18,22]}
df=pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nMissing Values:")
print(df.isnull())