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

    if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
        return True

    if matrix[r][c][1] != 0:
        return True

    # Zmieniamy stan na 'otwarta' (stan 1)
    matrix[r][c][1] = 1

    if matrix[r][c][0] == -1:
        return False

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

def get_start_settings(level_name):
    """
    Określa rozmiar planszy na podstawie wybranego poziomu trudności.
    """
    levels = {
        "łatwy": 4,
        "średni": 8,
        "trudny": 16
    } 
    size = levels.get(level_name.lower(), 8)
    return size

def restart_current_game(current_size):
    """
    Logika dla przycisku 'restart' w trakcie gry.
    Tworzy nową macierz o tym samym rozmiarze.
    """
    return matrix_generacia(current_size)

def handle_end_game(user_choice, current_size):
    """
    Obsługuje wybór gracza po wygranej lub przegranej.
    """
    if user_choice == "Kontynuuj":
        return matrix_generacia(current_size), current_size
    
    elif user_choice == "Zmien trudnosc":
        return "ZMIEN_POZIOM", None
        
    elif user_choice== "Wyjdz":
        return "WYJDZ", None




