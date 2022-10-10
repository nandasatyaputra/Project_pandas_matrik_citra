import pandas as pd

# Create list
fruits_list = [['Apple', 'Banana', 'Orange', 'Mango'],[120, 40, 80, 500]]
print(fruits_list)

# Create DataFrame from list
fruits_df = pd.DataFrame(fruits_list)
print(fruits_df)