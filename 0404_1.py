# NN -> Matrix 곱
# minimize_w(eight) Loss -> SE(Y-Yhat), BCE/NLL, Softmax

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[1]])
Y = np.array([[0],[0],[0],[1]])

def dataLoader(x, y, n=1):
    D = np.random.permutation(np.c_[x,y])

    for i in range(len(x)//n):
        yield (D[i*n:i*n+n,:-1], D[i*n:i*n+n,-1:])

def logistic(x):
    return 1/(1+np.exp(-x))

def dlogistic(x):
    return logistic(x)*(1-logistic(x))

# Activate Func. = Logistic, Single Layer Perceptron = 단층뉴럴네트웤
# J = NLL/BCE => -(ylogp-(1-y)log(1-p)) => -(y-p)

# W = np.random.rand(X.shape[-1], Y.shape[-1])
# B = np.random.rand(Y.shape[-1])

# lr = 1e-5
# epoch = 100000

# N = 4
# J = lambda y, _y : -(y*np.log(_y)-(1-y)*np.log(1-_y))

# loss = list()

# for i in range(epoch):
#     for x, y in dataLoader(X, Y, N):

#         z = x @ W + B
#         Yhat = logistic(z)

#         dLoss = -(y- Yhat)  # Yhat-Y = -(Y-Yhat)
#         dZ = dlogistic(z)*dLoss
#         dB = np.sum(dZ)
#         dW = x.T @ dZ
#         B = B - lr*dB
#         W = W - lr*dW

#     if epoch % 100 == 0:
#         loss.append(np.sum(J(Y, logistic(X@W+B))))

# plt.plot(loss)
# logistic(X@W+B)

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-2
epoch = 100000

N = 4
J = lambda y, _y : -(y*np.log(_y)+(1-y)*np.log(1-_y))

loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, N):
        # Feed forward
        z = x @ W + B # (N,2)*(2,1)+(1,) => (N,1)+(1,) => (N,1)
        Yhat = logistic(z)
        # Back propagation
        dLoss = -(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dZ = dlogistic(z)*dLoss
        dB = np.sum(dZ)
        dW = x.T @ dZ
        B = B - lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        loss.append(np.sum(J(Y, logistic(X@W+B))))

plt.plot(loss)
logistic(X@W+B) > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-2
epoch = 100000

N = 4
J = lambda y, _y: -(y*np.log(_y)+(1-y)*np.log(1-_y))

loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, N):
        # Feed forward
        z = x @ W + B # (N,2)*(2,1)+(1,) => (N,1)+(1,) => (N,1)
        Yhat = logistic(z)

        # Back propagation
        dLoss = -(y - Yhat)
        dZ = dlogistic(z)*dLoss
        dB = np.sum(dZ)
        dW = x.T @ dZ
        B = B - lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        loss.append(np.sum(J(Y, logistic(X@W+B))))

plt.plot(loss)
logistic(X@W+B) > .5



X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[1]])
N = np.array([[0],[0],[0],[1]])



Y = np.array([[0,0],[1,1],[1,1],[1,2]])

def dataLoader(x, y, n=1):
    D = np.random.permutation(np.c_[x,y])

    for i in range(len(x)//n):
        yield (D[i*n:i*n+n,:-2], D[i*n:i*n+n,-2:])

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-2
epoch = 100000

N = 4
J1 = lambda y, _y: -(y*np.log(_y)+(1-y)*np.log(1-_y))
J2 = lambda y, _y: (y-_y)**2

loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, N):
        z = x @ W + B # (N,2) (2,2) + (2,)
        Yhat1 = logistic(z[:,:1]) # (N,1)
        Yhat2 = z[:,1:] # (N,1)

        dLoss1 = -(y[:,:1] - Yhat1)
        dLoss2 = -(y[:,1:] - Yhat2)
        dZ = dlogistic(z)*dLoss1
        dB = np.sum(dZ)+np.sum(dLoss2)
        dW = x.T @ dZ + x.T @ dLoss2

        B = B - lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        loss.append(np.sum(J1(Y, logistic(X@W+B)[:,:1]))+np.sum(J2(Y, (X@W+B)[:,1:])))

plt.plot(loss)

logistic(X@W+B)[:, :1] > .5, logistic(X@W+B)[:, 1:]





def softmax(x) :
    xmax = np.max(x, axis=1)
    return xmax

softmax(np.array([[0,1],[1,0],[2,2]]))

def softmax(x) :
    xmax = np.max(x, axis=1, keepdims=1)
    _x = x - xmax
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

softmax(np.array([[0,1],[1,0],[2,2]]))

def softmax(x) :
    xmax = np.max(x, axis=1, keepdims=1)
    _x = x - xmax
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

softmax(np.array([[1,1],[2,1],[2,2]]))

Y = np.array([[0,0],[0,1],[0,1],[0,1]])

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-4
epoch = 30000

N = 4
J = lambda y, _y : -np.sum(y*np.log(_y))

loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, N):
        Z = x @ W + B
        Yhat = softmax(Z)

        dLoss = -(y - Yhat)  # Yhat-Y = -(Y-Yhat)

        dB = np.sum(dLoss)
        dW = x.T @ dLoss
        B = B - lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        loss.append(np.sum(J(Y, softmax(X@W+B))))

loss[-1]

plt.plot(loss)

softmax(X@W+B) > .5



Y = np.array([[1,0],[0,1],[0,1],[1,0]])

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-4
epoch = 300000

N = 4
J = lambda y, _y : -np.sum(y*np.log(_y))

loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, N):
        Z = x @ W + B
        Yhat = softmax(Z)

        dLoss = -(y - Yhat)  # Yhat-Y = -(Y-Yhat)

        dB = np.sum(dLoss)
        dW = x.T @ dLoss
        B = B - lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        loss.append(np.sum(J(Y, softmax(X@W+B))))

loss[-1]

plt.plot(loss)

softmax(X@W+B) > .5



Y = np.array([[0],[1],[1],[0]])

def dataLoader(x, y, n=1):
    D = np.random.permutation(np.c_[x,y])

    for i in range(len(x)//n):
        yield (D[i*n:i*n+n,:-1], D[i*n:i*n+n,-1:])

N = 4
H = 2

W1 = np.random.rand(X.shape[-1], H)
B1 = np.random.rand(H)

W2 = np.random.rand(H, Y.shape[-1])
B2 = np.random.rand(Y.shape[-1])

lr = 1e-2
epoch = 30000

J = lambda y, _y: np.sum((y-_y)**2)

loss = list()

# Multi Layer Perceptron;
# Hidden Layer; Activate Func.(Sigmoid-Logistic/tanh)
# Output Layer; 값으로 비교 => P(Logistic)
#            or P 분포(Softmax) 출력값 노드 2개 이상
for i in range(epoch):
    for x, y in dataLoader(X, Y, N):
        Z1 = x @ W1 + B1 # (N,2) (2,H) + (H,)
        X2 = logistic(Z1)

        Z2 = X2 @ W2 + B2 # (N,H) (H,1) + (1,)

        dLoss = -(y - Z2) # SE

        dB2 = np.sum(dLoss)
        dW2 = X2.T @ dLoss

        dZ2 = dLoss @ W2.T # (N,1) (1,H) = N,H
        dZ1 = dlogistic(Z1) * dZ2
        dB1 = np.sum(dZ1)
        dW1 = x.T @ dZ1 # (2, N) * (N,H)

        B2 = B2 - lr*dB2
        W2 = W2 - lr*dW2

        B1 = B1 - lr*dB1
        W1 = W1 - lr*dW1

    if epoch % 100 == 0:
        loss.append(np.sum(J(Y, logistic(X@W1+B1)@W2+B2)))

loss[-1]

plt.plot(loss)
logistic(X@W1+B1)@W2+B2 > .5



