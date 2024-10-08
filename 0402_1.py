import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'



import numpy as np

import matplotlib.pyplot as plt

np.pi

X = np.linspace(0, np.pi/2, 100)

X

Y = np.cos(X)

plt.plot(X, Y)

X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

plt.plot(X, Y)
plt.plot(X, np.dot(X, Theta))



X = np.linspace(0, np.pi/2, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

Theta

plt.plot(X, Y)
plt.plot(X, np.dot(X, Theta))



X = np.linspace(0, np.pi, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

Theta

plt.plot(X, Y)
plt.plot(X, np.dot(X, Theta))



X = np.linspace(0, np.pi*2, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

Theta

plt.plot(X, Y)
plt.plot(X, np.dot(X, Theta))



X = np.linspace(-np.pi*2, np.pi*2, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

plt.plot(X[:,1], Y)
plt.plot(X[:,1], np.dot(X, Theta))



X = np.linspace(0, np.pi*2, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X, np.power(X, 2), np.power(X, 3), np.power(X, 4), np.power(X, 5)]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

Theta

plt.plot(X[:,1], Y)
plt.plot(X[:,1], np.dot(X, Theta))



X = np.linspace(-np.pi*2, np.pi*2, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X, np.power(X, 2), np.power(X, 3), np.power(X, 4), np.power(X, 5)]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

Theta

plt.plot(X[:,1], Y)
plt.plot(X[:,1], np.dot(X, Theta))



X = np.linspace(0, np.pi*2, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

Theta

plt.plot(X[:,1], Y)
plt.plot(X[:,1], np.dot(X, Theta))



X = np.linspace(0, np.pi*2, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X, np.power(X, 2), np.power(X, 3), np.power(X, 4), np.power(X, 5)]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

Theta

plt.plot(X[:,1], Y)
plt.plot(X[:,1], np.dot(X, Theta))



X = np.linspace(-np.pi*2, np.pi*2, 100)

Y = np.cos(X)

X = np.c_[np.ones(len(X)), X, np.power(X, 2), np.power(X, 3), np.power(X, 4), np.power(X, 5)]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

plt.plot(X[:,1], Y)
plt.plot(X[:,1], np.dot(X, Theta))



X = np.linspace(0, np.pi*2, 100)
X[np.cos(X) < 0] = 0
X[np.cos(X) > 0] = 1

X



X = np.linspace(0, np.pi, 100)
Y = np.ones(len(X))
Y[np.cos(X) < 0] = 0

Y

X = np.c_[np.ones(len(X)), X]

Theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

plt.plot(X[:,1], Y)
plt.plot(X[:,1], np.dot(X, Theta))

plt.plot(X[:,1], np.cos(X[:,1]))
plt.plot(X[:,1], np.dot(X, Theta))

plt.plot(X[:,1], np.cos(X[:,1]))
plt.plot(X[:,1], np.dot(X, Theta))
plt.axhline(.5, c='red')
plt.axvline(.5, c='red')

plt.plot(X[:,1], np.cos(X[:,1]))
plt.plot(X[:,1], np.dot(X, Theta))
plt.axhline(.5, c='red')
plt.axvline(-Theta[0]/Theta[1], c='red')

plt.plot(X[:,1], np.cos(X[:,1]))
plt.plot(X[:,1], np.dot(X, Theta))
plt.axhline(.5, c='red')
plt.axvline(-Theta[1]/Theta[0], c='red')

plt.scatter(X[:,1], Y)
plt.plot(X[:,1], np.dot(X, Theta))
plt.axhline(.5, c='red')
plt.axvline((.5-Theta[0])/Theta[1], c='red')



np.array([1, np.pi*3]).dot(Theta)

np.array([1, np.pi*3]).dot(Theta) > .5

np.array([1, np.pi*1/4]).dot(Theta) > .5

np.array([1, -np.pi]).dot(Theta) > .5



from math import exp

from math import factorial

X = list(range(10))

plt.plot(X, [exp(x) for x in X])

a = 1 # 특정점

def taylor(x, N=2):
    rst = 0.0
    for n in range(N):
        rst += (exp(a)/factorial(n)*(x-a)**n)
    return rst

plt.plot(X, [exp(x) for x in X])
plt.plot(X, [taylor(x, 10) for x in X])

plt.plot(X, [exp(x) for x in X])
plt.plot(X, [taylor(x, 2) for x in X])

plt.plot(X, [exp(x) for x in X])
plt.plot(X, [taylor(x, 50) for x in X])



# rosenbrock

fn = lambda x1, x2 : ((1-x1)**2) + 100*((x2-x1**2)**2)


dx1 = lambda x1, x2 : -2*(1-x1)-400*x1*(x2-x1**2)
dx2 = lambda x1, x2 : 200*(x2-x1**2)

from math import sqrt

h = 1e-3
xt = (-1.3, 0.9)

for i in range(1):
    dxt = (dx1(*xt), dx2(*xt))
    vl = sqrt(dxt[0]**2+dxt[1]**2)
    u = (dxt[0]/vl, dxt[1]/vl)
    nx1 = xt[0] - h*u[0]
    nx2 = xt[1] - h*u[1]
    xt = (nx1, nx2)

xt, fn(*xt)

h = 1e-3
xt = (-1.3, 0.9)

for i in range(10000):
    dxt = (dx1(*xt), dx2(*xt))
    vl = sqrt(dxt[0]**2+dxt[1]**2)
    u = (dxt[0]/vl, dxt[1]/vl)
    nx1 = xt[0] - h*u[0]
    nx2 = xt[1] - h*u[1]
    xt = (nx1, nx2)

xt, fn(*xt)

# https://datascienceschool.net/02%20mathematics/05.01%20%EC%B5%9C%EC%A0%81%ED%99%94%20%EA%B8%B0%EC%B4%88.html



logisitc1 = lambda x:1/(1+np.exp(-x))
logisitc2 = lambda x: np.exp(x)/(1+np.exp(x))

X = np.linspace(-3, 3, 100)

plt.plot(X, logisitc1(X), c = 'r')
plt.plot(X, logisitc2(X), c = 'b')

X = np.linspace(0, np.pi)

X

X = np.linspace(0, np.pi)
Y = np.ones(len(X))
Y[np.cos(X) < 0 ] = 0

plt.scatter(X, Y)

plt.scatter(X, Y)
plt.plot(X, logisitc1(X))



X = np.c_[np.ones(len(X)), X]

X

Theta = np.array([1,1])

Theta



plt.scatter(X[:,1], Y)
plt.plot(X[:,1], logisitc1(X.dot(Theta)))

logisitc1(X.dot(Theta))

X = np.linspace(0, np.pi)
Y = np.ones(len(X))
Y[np.cos(X) < 0] = 0
X = np.c_[np.ones(len(X)), X]

Theta = np.array([1,1])
h = 1e-5
for i in range(100000):
    d = Y-logisitc1(X.dot(Theta))
    Theta = Theta + h*(X.T.dot(d)/np.linalg.norm(X.T.dot(d)))#/len(X)
Theta

plt.scatter(X[:,1], Y)
plt.plot(X[:,1], logisitc1(X.dot(Theta)))

logisitc1(X.dot(Theta))

