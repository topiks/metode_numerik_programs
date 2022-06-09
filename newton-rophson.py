def fungsi(x): return 0.5*x*x-3*x-2
def turunan(x): return x-3


f1 = 0.0005*x**4 + 0.022 * x**2 + 0.111*x - 0.67185


def newtonraphson(f, ft, xt, eps=1e-5):
    while abs(f(xt)) > eps:
        xp = xt
        xt = xt - (f(xt)/ft(xt))
        if abs(xp-xt) < eps:
            break
    return xt


print(newtonraphson(f1, turunan, 5))
print(fungsi(6.605551290258319))
