import pandas as pd
from sklearn.cluster import KMeans

data = {
    'Customer':['A','B','C','D','E'],
    'Age': [20,30,40,22,31],
    'Spending':[100,200,300,110,290]
}

df = pd.DataFrame(data)
X = df[['Age','Spending']]
model = KMeans(n_clusters = 2, random_state = 42,n_init=10)
#n_init means clustering refining process will be executed 10 times

df['Group'] = model.fit_predict(X)
print(df)