from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

X = [1,0,1,1,0,1,0]
y = [1,0,1,0,0,1,1]
print("Accuracy: ",accuracy_score(X,y))
print("Precision: ",precision_score(X,y))
print("Recall: ",recall_score(X,y))
print("F1 Score: ",recall_score(X,y))