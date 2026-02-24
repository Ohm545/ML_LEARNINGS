import pandas as pd

data = {
    'Name': ['Ohm', 'ABC', 'XYZ'],
    'Age': [25,None,23],
    'Salary':[50000, 60000,None]
}

df = pd.DataFrame(data)
print("Original data")
print(df)

print(df.isnull().sum()) # Returns total null values per col.
df_drop = df.dropna() # drop the null value containing rows.
print(df_drop) 

df['Age'].fillna(df['Age'].mean(), inplace = True) # Replace null with the Mean value of that col
df['Salary'].fillna(df['Salary'].mean(),inplace = True) # Replace null with the Mean value of that col
print(df)
