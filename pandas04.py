import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

# drop column
student_df = student_df.drop(columns='age')

print(student_df)