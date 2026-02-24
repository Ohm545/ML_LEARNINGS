from sklearn.neighbors import KNeighborsClassifier

X = [
    [100,7],[200,7.5],[250,8],[300,8.5],[330,9],[360,9.5]
]
y = [0,0,0,1,1,1]

model = KNeighborsClassifier(n_neighbors = 4)

model.fit(X,y)

pred = model.predict([[275,8.5]])
print(pred)