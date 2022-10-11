import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry',],
                 'Age':  [20, 21, 19],
                'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)

value = student_df.iat[2,1] * student_df.iat[0,1]
value2 = student_df.iat[1,2]  ## kolom , baris
print(value) # --> Output: 77.80
print(value2) #hasil gabung