from sklearn.linear_model import LogisticRegression

x = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1]

model = LogisticRegression()

model.fit(x,y)

hours = float(input("Enter number of hours you studied: "))
result = model.predict([[hours]])

if result == 1:
    print("You are likely to pass the examination")
else :
    print("You are likely to failed the examination")