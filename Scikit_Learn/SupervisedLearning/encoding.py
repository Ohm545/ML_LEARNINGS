from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("student.csv")
df_label = df.copy()
le = LabelEncoder()
df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender'])
df_label['Result_Encoded'] = le.fit_transform(df_label['Result'])

#fit_transform -> fit means learn from the data and after learning fill that value in that col.

# One hot encoding

df_encoded = pd.get_dummies(df_label,columns=['City'])
print(df_encoded)

#get_dummies -> replace the categorical data into numerical format. 
