# https://stackoverflow.com/questions/3514283/c-tail-call-optimization



# stack, FILO
# que, FIFO

# CPYTHON, Jypthon, Python for NET, IronPython, PyPy



# 함수의 꼬리 재귀 호출(Tail Recursion)

# 피보나치 수



# Commented out IPython magic to ensure Python compatibility.
# %timeit sum([i for i in range(1000000)])

# Commented out IPython magic to ensure Python compatibility.
# %timeit sum((i for i in range(1000000)))

# Commented out IPython magic to ensure Python compatibility.
# %timeit sum(i for i in range(1000000))



# first class : value
# 1. a = x
# 2. a[x], {'a':x}
# 3.
# ...
# 10. fun(x):
# 11. def a():
#       return x

def x():
    return 1



# closoure

def t():
    def y():
        return 1
    return y()

t()

t()()

def t():
    def y(m):
        return m
    return y

t()

t()()

t()(3)

def t(n):
    def y(m):
        return m+n
    return y

t(1)(4)

xx = t(1)

xx(3)



# function closoure = decorator  -->> tf.function 도 그 중 하나인데 매우 어려움.



# lamda - 스택에서 한번 쓰고 버릴때 주로 사용한다

a = lambda x : 1

a.__name__



# 3*4
# 3**4
# a, *b = 1,2,3,
# def fun(*)
# def fun(*arg)
# def fun(**arg)
# fun(*arg)
# {*, }
# from import *

# function
# class
# class __call__ 의 object

def x():
    print(1)

callable(x)

callable(int)

1()

dir(print)



# 이름이 있는 함수와 람다 함수, 메소드 함수 등등

a = x

a.__name__



adders = []
for n in range(5):
    adders.append(lambda m : m+n)

adders

adders[2](1)



a = 1
a = 2
a = 3

a



def x(b, a = []):
    return a.append(b)

x(3)



def xx():
    return 1

xx()



# mutable return 값은 3종류

a = [1,2,3,4]

a.append(5)

a

a.index(3)

a

a.pop(1)

a



def x(b, aa = []):
    return a.append(b)

aa

bb = []
x(3,bb)

bb



def xx(b, aa = []):
    c = aa.append(b)
    return c

xx(3)



def f(a, L=[]):
    L.append(a)
    return L

f(1)

f(2) #mutable의 특징, 디폴트 값 공유

def ff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

ff(1)

ff(2)



import time

time.time()

def tt(t=time.time()):
    return t

tt()



