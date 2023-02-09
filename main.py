import scipy.integrate as itg

print('hello world !!!')
print('hello PI2C')
print('hello in main')

def f(x):
    return x*x

print(itg.quad(f, 1, 3)[0])