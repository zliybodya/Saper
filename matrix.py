#m[wiersz][kolumna][stan, otwarta czy flaga czy nie otwarta]
#stan -1 = bomba; [1; 8] = liczba bomb obok


import random
import math

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
def clear_safe_zone(matrix, r, c):
    rozmiar = len(matrix)
    # Liczymy i usuwamy miny z kwadratu 3x3
    bomb_count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            ni = r + dx
            nj = c + dy
            if 0 <= ni < rozmiar and 0 <= nj < rozmiar:
                if matrix[ni][nj][0] == -1:
                    matrix[ni][nj][0] = 0
                    bomb_count = bomb_count + 1
    
    # Umieszczamy znalezione miny w innych miejscach
    placed = 0
    while placed < bomb_count:
        a = random.randint(0, rozmiar - 1)
        b = random.randint(0, rozmiar - 1)
        is_in_safe_zone = False
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if a == r + dx and b == c + dy:
                    is_in_safe_zone = True
                    break
            if is_in_safe_zone:
                break
        
        if not is_in_safe_zone and matrix[a][b][0] != -1:
            matrix[a][b][0] = -1
            placed = placed + 1
    
    for i in range(rozmiar):
        for j in range(rozmiar):
            if matrix[i][j][0] != -1:
                matrix[i][j][0] = 0
    for i in range(rozmiar):
        for j in range(rozmiar):
            if matrix[i][j][0] == -1:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni = i + dx
                        nj = j + dy
                        if 0 <= ni < rozmiar and 0 <= nj < rozmiar:
                            if matrix[ni][nj][0] != -1:
                                matrix[ni][nj][0] += 1