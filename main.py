import scipy.integrate as itg

def add(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError('{} is not a number'.format(a))
    if not isinstance(b, (int, float)):
        raise TypeError('{} is not a number'.format(b))
    return a + b

print('hello world !!!')
print('hello PI2C')
print('hello in main')

def f(x):
    return x*x

print(itg.quad(f, 1, 3)[0])