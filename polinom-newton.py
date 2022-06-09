import numpy as np

data = [[0, 1], [1, 0.5403], [2, -0.4161], [3, -0.9900], [4, -0.6536]]
target = 2.5


def polinomNewton(databuffer, targetbuffer):
    orde = len(databuffer)
    penampungan = np.zeros(shape=(len(databuffer) - 1, len(databuffer) - 1))
    for i in range(2):
        for j in range(orde-1):
            if i == 0:
                hasil = (databuffer[j+1][1] - databuffer[j][1]) / \
                    (databuffer[j+1][0] - databuffer[j][0])
                penampungan[i][j] = hasil

            # print(databuffer[j+1][1], " - ",  databuffer[j][1])
        # print("---")

    for k in range(1):
        for m in range(len(penampungan[0])-1):
            hasil = (penampungan[k][m+1] - penampungan[k][m])
            # print(databuffer[k][m+1], " - ",  databuffer[k][m], " = ")
            print(m)

            # print(penampungan[k][m])
            # hasil = penampungan[k+1] - penampungan[k]

    # print(penampungan)


polinomNewton(data, target)
