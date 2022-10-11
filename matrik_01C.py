import pandas as pd

# Create hierarchical dict
student_dict = {"Grade A": {'Class A': {'name': 'Joe', 'marks': 91.56},
                            'Class B': {'name': 'Harry', 'marks': 87.90}},
                "Grade B": {'Class A': {'name': 'Sam', 'marks': 70},
                            'Class B': {'name': 'Alan', 'marks': 65.48}}}
print(student_dict)

# Create multi-index DataFrame
student_df = pd.DataFrame.from_dict({(i, j): student_dict[i][j]
                                     for i in student_dict.keys()
                                     for j in student_dict[i].keys()},
                                    orient='index')
print(student_df)
