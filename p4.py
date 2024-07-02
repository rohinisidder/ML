import numpy as np
X = np.array(([2,9],[1,5],[3,6]),dtype=float)
y = np.array(([92],[86],[89]),dtype=float)
X = X/np.amax(X,axis=0)
y = y/100
epoch = 1000
eta = 0.2
input = 2
hidden = 3
output = 1
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_grad(x):
    return x*(1-x)
wh = np.random.uniform(size=(input,hidden))
bh = np.random.uniform(size=(1,hidden))
wout = np.random.uniform(size=(hidden,output))
bout = np.random.uniform(size=(1,output))
for i in range(epoch):
    h_ip = np.dot(X,wh) + bh
    h_act = sigmoid(h_ip)
    o_ip = np.dot(h_act,wout) + bout
    output = sigmoid(o_ip)
    E0 = y - output
    output_grad = sigmoid_grad(output)
    d_output = E0*output_grad
    Eh = d_output.dot(wout.T)
    hidden_grad = sigmoid_grad(h_act)
    d_hidden = Eh*hidden_grad

    wout+=h_act.T.dot(d_output)*eta
    wh+=X.T.dot(d_hidden)*eta

print("Normalized input"+str(X))
print("actual output"+str(y))
print("predicted ouput",output)