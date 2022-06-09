#Import math Library
import math
def secant(f, a, b):
    x= a -(f(a)*(a-b))/(f(a)-f(b))
    return x, abs(x-a)
f = lambda x: math.exp(x) - 5 * x**2
xr = [0.5, 1]
i = 1
while abs(f(xr[i])) >= 0.00001:
    a, b=secant(f, xr[i], xr[i-1])
    xr.append(round(a, 9))
    print(a)
    i += 1
#fungsi secant untuk mencari nilai Xr+1
#fungsi f(x)
#list berisi nilai xr


