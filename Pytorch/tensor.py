import torch
print(torch.__version__)
x = torch.tensor([1,2,3,4]) # list past to function to create tensor 
print(x) # 1D tensor
y = torch.tensor([[1,2],[3,4]])
print(y) # 2D tensor
z = torch.zeros(3,2) #(rows,cols)
print(z)
a = torch.ones(2,2) #(rows,cols)
print(a)
r = torch.rand(3,3) # random values
print(r) 

#indexing 
i = torch.tensor([10,20,30])
print(i[0])
k = torch.tensor([20,30,50])
j = torch.tensor([[10,20],[30,40]])
print(j[0,1]) # [row,col]
 
print(i+k)
print(i*k)