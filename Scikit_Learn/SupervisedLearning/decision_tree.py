from sklearn.tree import DecisionTreeClassifier

X = [
    [7,2],
    [8,3],
    [9,8],
    [10,9]
]

y = [0,0,1,1]

model = DecisionTreeClassifier()

model.fit(X,y)

size = float(input("Enter the size in cm: "))
shade = float(input("Enter the color shade(1-10): "))

result = model.predict([[size,shade]])[0]

print(result)