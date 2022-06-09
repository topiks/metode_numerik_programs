def f1(x): return 3/(x-2)
def f2(x): return (x**2 - 3)/2


def lelaran(f, tebakan, eps=1e-6):
    counter = tebakan
    maksimalIterasi = 30
    i = 0
    if tebakan < eps:
        return tebakan
    else:
        while i <= maksimalIterasi:
            counter_sesudah = f(counter)
            pengurangan = abs(counter_sesudah - counter)
            print(counter_sesudah, pengurangan)
            counter = counter_sesudah
            i = i + 1
            if pengurangan < eps:
                break
            if i == maksimalIterasi:
                return print("divergen")

        return 0


lelaran(f1, 4)
