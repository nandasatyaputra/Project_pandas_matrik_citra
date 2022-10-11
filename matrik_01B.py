# import pandas library
import pandas as pd

# Create dict object
student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": ["85", "77", "91.54"]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("DataFrame with inferred data type : \n", student_df.dtypes)

student_df = pd.DataFrame(student_dict, dtype="float64")
print("DataFrame with changed data type : \n", student_df.dtypes)

print(student_df)