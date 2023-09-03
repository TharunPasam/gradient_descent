import numpy as np

def gradient_descent (x,y):
  w = b = 0
  iterations = 1000
  learning_rate = 0.001
  for i in range (iterations):
    y_predicted = w * x + b 
    cost = (1/n) * sum([val **2 for val in (y-y_predicted)])
    wd = -(2/n) * sum(x*(y-y_predicted))
    bd = -(2/n) * sum(y-y_predicted)
    w = w - learning_rate * wd
    b = b - learning_rate * bd
    print("w{},b{},cost{},iterations{}".format(w,b,cost,i))
          

x = np.array ([1,2,3,4,5])
y = np.array ([6,7,8,9,10])


gradient_descent (x,y)