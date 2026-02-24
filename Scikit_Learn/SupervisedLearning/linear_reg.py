from sklearn.linear_model import LinearRegression
model = LinearRegression()
X = [[1],[2],[3],[4],[5]]
y = [40,50,60,70,80]
model.fit(X,y)
hours = float(input("Enter number of hours you study"))
marks_pred = model.predict([[hours]])
print(f"Based on your hours {hours} you may scored {marks_pred}")