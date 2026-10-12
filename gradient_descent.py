import numpy as np

def gradient_descent(x, y):

    m = 0
    b = 0

    iterations = 500
    n = len(x)
    learning_rate = 0.08

    for i in range(iterations):
        y_pred = m * x + b

        #cost
        cost = (1/n)*sum([val**2 for val in (y - y_pred)]) 

        D_m = -(2/n) * sum(x * (y - y_pred)) #derivative with respect to m
        D_b = -(2/n) * sum(y - y_pred) #derivative with respect to b

        #updating m 
        m = m - learning_rate * D_m

        #updating b
        b = b - learning_rate * D_b

        print(f"Iteration{i}: m = {m:.4f}: b ={b:.4f},Cost ={cost:.4f}")

x = np.array([1,2,3,4,5])

y = np.array([5,7,9,11,13])

gradient_descent(x,y)