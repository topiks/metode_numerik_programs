def fungsi(x): return 0.5*x*x-5*x-2


def f1(x): return 0.0005*x**4 + 0.022 * x**2 + 0.111*x - 0.67185


def secant(f, a, b, eps=1e-5):
    # i = 0
    # a atas / bilangan kedua / xn
    # b bawah / bilangan pertama / xn-1
    # while abs(f(a)) > eps:
    #     if abs(f(b)) < eps:
    #         return b
    #     if abs(f(a)) < eps:
    #         return a
    for i in range(6):
        c = a - ((f(a)*(a-b))/(f(a)-f(b)))
        b = a
        a = c

        print(i, c, f(c))
        # i = i + 1
    return c


akar = secant(f1, 4, 0)
print("\n", f1(akar), akar)
