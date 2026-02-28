import torch

w = torch.tensor(2.0, requires_grad = True) # this parameter will create impact

x = torch.tensor(5.0)

y_pred = w*x

y_true = torch.tensor(16.0)
loss = (y_pred - y_true)**2
print(loss)
loss.backward() # result of this get stored in w.grad()
print(w.grad)

