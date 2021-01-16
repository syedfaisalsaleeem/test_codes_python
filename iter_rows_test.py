import pandas as pd 
  
# Creating a data frame 
df = pd.DataFrame([['Animal', 'Baby', 'Cat', 'Dog', 
                    'Elephant', 'Frog', 'Gragor']]) 
  
# Itering over the data frame rows 
# using df.iterrows() 
# itr = next(df.iterrows()) 
# print(itr) 

# for index,values in df.iterrows():
# 	print(index,"index",values)

import pandas as pd

df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})

for index, row in df.iterrows():
    # print(row['c1'], row['c2'])
    print(row,index)