data = [[0, 1], [0.4, 0.921061], [0.8, 0.696707], [1.2, 0.362358]]
target = 0.5

data2 = [[1, 1.5709], [4, 1.5727], [6, 1.5751]]
target2 = 3.5

data3 = [[1, 0.4625], [2, 0.64924], [3, 0.90609],
         [4, 1.26456], [5, 1.76483], [6, 2.46302]]
target3 = 2.4
target4 = 3.55
target5 = 4.7

data4 = [[0, 1], [0.4, 0.92], [0.8, 0.69], [1.2, 0.36]]
target6 = 0.5

data10 = [[-1, -0.16667], [0, -1], [1, 1.3],
          [2, -1.333], [3, -1, 214], [4, -1]]
target10 = 3.5


def lagrange(databuffer, targetbuffer):
    atas = 1
    bawah = 1
    data_bawah = []
    data_atas = []
    hasil = 0
    orde = len(databuffer)

    for j in range(orde):
        for k in range(orde):
            kecuali = databuffer[j][0]
            data_masuk = databuffer[k][0]
            if data_masuk != kecuali:
                atas = atas * (targetbuffer - data_masuk)
                bawah = bawah * (kecuali - data_masuk)
        data_bawah.append(bawah)
        data_atas.append(atas)
        atas = 1
        bawah = 1

    for i in range(len(data_atas)):
        hasil = hasil + databuffer[i][1] * data_atas[i] / data_bawah[i]

    print(hasil)


lagrange(data10, target10)
