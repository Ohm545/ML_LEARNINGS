from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'StudyHours':[1,2,3,4,5],
    'TestScore':[40,50,60,70,80]
}

df = pd.DataFrame(data)

standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df)
scaled_df = pd.DataFrame(standard_scaled, columns=['StudyHours','TestScore'])
print(scaled_df)

minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)
scaled_df = pd.DataFrame(minmax_scaled, columns=['StudyHours','TestScore'])
print(scaled_df)

#Training

x = df[['StudyHours']]
y = df[['TestScore']]

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size = 0.2,random_state=42)

# train_test_split -> split the data to test and train 
# split the data as per test_size and random_state means always use fix set of records for training
# and for testing

print(X_train)
print(Y_train)
print(X_test)
print(Y_train)