#m[wiersz][kolumna][stan, otwarta czy flaga czy nie otwarta]
#stan -1 = bomba; [1; 8] = liczba bomb obok


import random
import math

rozmiar = 8


def matrix_generacia(rozmiar):
    matrix = []
    for ii in range(rozmiar):
        a = []
        for jj in range(rozmiar):
            b = [0, 0]
            a.append(b)
        matrix.append(a)
    liczba_bomb = math.floor(rozmiar * rozmiar * 0.2)
    h = 0
    while h < liczba_bomb:
        a = random.randint(0, rozmiar - 1)
        b = random.randint(0, rozmiar - 1)
        if matrix[a][b][0] != -1:
            matrix[a][b][0] = -1
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ni = a + dx
                    nj = b + dy
                    if 0 <= ni < rozmiar and 0 <= nj < rozmiar:
                        if matrix[ni][nj][0] != -1:
                            matrix[ni][nj][0] += 1
            h = h +1


    return matrix
m = matrix_generacia(rozmiar)
for i in range(rozmiar):
    print(m[i])
