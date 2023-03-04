import pandas as pd
file_name = 'C:\\Users\\Admin\\Desktop\\task02\\input.xlsx'
df = pd.read_excel(file_name, skiprows=10, nrows=52)
print(df.head(62))
