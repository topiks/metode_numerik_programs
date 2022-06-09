def fungsi(x): return 0.5*x*x-3*x-2
def f2(x): return 2.718**x - 5*x**2


def falsepos(f, a, b, eps=1e-10):
    if abs(f(a)) < eps:
        return a
    elif abs(f(b)) < eps:
        return b
    else:
        c = b - ((f(b)*(b-a))/(f(b) - f(a)))
        while abs(f(c)) > eps:
            if f(c)*f(a) > 0:
                a = c
            else:
                b = c
            c = (a+b)/2
        return c


hasil = falsepos(fungsi, -5, 5, 1e-5)
print(hasil)
print(fungsi(hasil))
