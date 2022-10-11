
import pandas as pd
import numpy as np

df2 = {"a": [0, 1, 0], "b": [1, 1, 0]}

# Create DataFrame from dict
student_df2 = pd.DataFrame(df2)
print("Before dropping column NA: \n", student_df2)

# drop column with NaN
student_df3 = student_df2.dropna(axis='columns')

print("\nAfter dropping column NA: \n", student_df3)


# We pass a dict of {column name: column values}
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)

#data = pd.read_csv("student_data.csv")
#print(data)

data = {'satu': [1,1,1,1,1],
        'dua' : [2,2,2,2,2],
        'tiga': [3,3,3,3,3]}

df = pd.DataFrame(data)

print(df)

data = {'satu': [1,1,1,1,1],
        'dua' : [2,2,2,2,2],
        'tiga': [3,3,3,3,3]}

df1 = pd.DataFrame(data, index=['a','b','c','d','e']);

print(df1);



