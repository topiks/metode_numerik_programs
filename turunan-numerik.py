data = [[0, 0], [0.1, 0.0819], [0.2, 0.1341], [0.3, 0.1646], [0.4, 0.1797]]


def selisih_maju_h2(databuffer, target, h, orde):

    for i in range(len(databuffer)):
        for j in range(1):
            if databuffer[i][j] == target:
                orde_target = i

    data_pertama = databuffer[orde_target][1]
    data_kedua = databuffer[orde_target + 1][1]
    data_ketiga = databuffer[orde_target + 2][1]
    data_keebmpat = databuffer[orde_target + 3][1]
    data_kelima = databuffer[orde_target + 4][1]

    if orde == 1:
        print((-3*data_pertama + 4*data_kedua - data_ketiga)/2*h)
    elif orde == 2:
        print((2*data_pertama + -5*data_kedua + 4 *
              data_ketiga + -1*data_keebmpat)/h**2)
    elif orde == 3:
        print((-5*data_pertama + 18*data_keebmpat + -24 *
              data_ketiga + 14*data_keebmpat + -3*data_kelima)/2*h**3)

        # print(databuffer[orde_target][1])


def selisih_pusat_h2(databuffer, target, h, orde):

    for i in range(len(databuffer)):
        for j in range(1):
            if databuffer[i][j] == target:
                orde_target = i

    data_tengah = databuffer[orde_target][1]
    data_plus_satu = databuffer[orde_target + 1][1]
    data_plus_dua = databuffer[orde_target + 2][1]
    data_min_satu = databuffer[orde_target - 1][1]
    data_min_dua = databuffer[orde_target - 2][1]

    if orde == 1:
        print((data_plus_satu - data_min_satu)/2*h)
    elif orde == 2:
        print((-1*data_min_dua + 16*data_plus_satu - 30 *
              data_tengah + 16*data_min_satu - data_min_dua)/12*h**2)
    elif orde == 3:
        print((data_plus_dua - 2*data_plus_satu + 2 *
              data_min_satu - data_min_dua)/22*h**3)
    elif orde == 4:
        print((data_plus_dua - 4*data_plus_satu + 6 *
              data_tengah - 4*data_min_satu + data_min_dua)/h**4)


# selisih_maju_h2(data, 0.0, 0.1, 3)
selisih_pusat_h2(data, 0.2, 0.1, 4)
