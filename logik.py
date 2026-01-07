def toggle_flag(matrix, r, c):
    """Przełącza stan flagi na podanych współrzędnych"""
    # Jeśli komórka jest zamknięta (stan 0), stawiamy flagę (stan 2)
    if matrix[r][c][1] == 0:
        matrix[r][c][1] = 2
    # Jeśli flaga już tam jest (stan 2), zdejmujemy ją i zamykamy komórkę (stan 0)
    elif matrix[r][c][1] == 2:
        matrix[r][c][1] = 0


def open_cell(matrix, r, c):
    """Otwiera komórkę. Zwraca False, jeśli trafiono na minę, w przeciwnym razie True"""

    # Sprawdzenie, czy współrzędne mieszczą się w granicach macierzy
    if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
        return True

    # Jeśli komórka jest już otwarta lub oznaczona flagą, nic nie robimy
    if matrix[r][c][1] != 0:
        return True

    # Zmieniamy stan na 'otwarta' (stan 1)
    matrix[r][c][1] = 1

    # Jeśli trafiliśmy na minę (wartość -1), kończymy grę
    if matrix[r][c][0] == -1:
        return False

    # Jeśli komórka jest pusta (wartość 0), otwieramy sąsiadów rekurencyjnie
    if matrix[r][c][0] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Pomijamy samą komórkę środkową
                if dx == 0 and dy == 0:
                    continue
                # Wywołujemy funkcję dla wszystkich 8 sąsiadów
                open_cell(matrix, r + dx, c + dy)

    return True

def check_win(matrix):
    """Sprawdza, czy gracz odkrył wszystkie bezpieczne pola"""
    for row in matrix:
        for cell in row:
            # Jeśli pole NIE jest miną, a nadal jest zamknięte (0) lub ma flagę (2)
            if cell[0] != -1 and cell[1] != 1:
                return False # Jeszcze nie wygrano
    return True # Wszystkie bezpieczne pola są otwarte


#   Wizualizacja

def print_field(matrix, reveal_all=False):
    """Rysuje planszę w konsoli"""
    size = len(matrix)
    print("\n    " + " ".join(str(i).ljust(2) for i in range(size)))
    print("  " + "---" * size)

    for i, row in enumerate(matrix):
        line = f"{i} |"
        for cell in row:
            val, state = cell
            if reveal_all and val == -1:  # Pokaż wszystkie miny na końcu
                line += " * "
            elif state == 0:
                line += " . "  # Zakryte
            elif state == 2:
                line += " F "  # Flaga
            elif val == -1:
                line += " * "  # Mina (jeśli odkryta)
            elif val == 0:
                line += "   "  # Pustka
            else:
                line += f" {val} "  # Cyfra
        print(line)

m = matrix_generacia(rozmiar)
print_field(m)
