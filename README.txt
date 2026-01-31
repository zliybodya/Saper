PROJEKT: Gra Saper (Minesweeper)
-----------------------------------------
AUTORZY:
1. Yana Baiholava (nr albumu: 293635)
2. Bohdan Sul (nr albumu: 293637)
3. Roman Sydorenko (nr albumu: 293636)

OPIS PROJEKTU:
Klasyczna gra logiczna "Saper" zaimplementowana w języku Python. 
Celem gry jest odkrycie wszystkich pól, które nie zawierają min.

PLIKI:
- matrix.py: Logika generowania macierzy gry, rozmieszczanie min oraz obliczanie sąsiedztwa.
- logik.py: Logika przebiegu rozgrywki.
- grafic.py: Interfejs graficzny gry.
- start.bat: Plik wsadowy do szybkiego uruchomienia gry.
- import_lib.txt: Lista wymaganych bibliotek (obecnie pusty, ponieważ używamy bibliotek standardowych random i math).
- create_venv.bat: Skrypt do tworzenia środowiska wirtualnego Python (venv).

ANALIZA MODUŁU:
- matrix.py:
Plik ten odpowiada za matematyczną strukturę pola gry:
* Inicjalizacja: Tworzy macierz rozmiaru (rozmiar x rozmiar), gdzie 
  każda komórka przechowuje swój stan oraz status widoczności.
* Bezpieczny start: Dzięki funkcji is_safe_zone, miny nie są generowane 
  w bezpośrednim sąsiedztwie pierwszego kliknięcia gracza.
* Rozmieszczenie bomb: Liczba min wynosi zawsze 20% powierzchni pola.
* Obliczanie sąsiedztwa: Dla każdej miny program automatycznie 
  zwiększa licznik w sąsiednich ośmiu komórkach.

- logik.py:
Ten moduł steruje mechaniką gry:
* Obsługa flag: Funkcja toggle_flag pozwala graczowi oznaczać pola podejrzane o bycie minami.
* Odkrywanie pól: Funkcja open_cell wykorzystuje algorytm rekurencyjny do automatycznego otwierania pustych obszarów planszy.
* Warunek zwycięstwa: Funkcja check_win sprawdza, czy wszystkie bezpieczne pola zostały odkryte.
* Zarządzanie poziomami: Definiuje rozmiary planszy dla trzech poziomów trudności (4x4, 8x8, 16x16).

- grafic.py:
Moduł ten odpowiada za interfejs graficzny użytkownika (GUI) przy użyciu biblioteki tkinter:
* Rendering: Dynamiczne rysowanie pola gry na komponencie Canvas przy użyciu autorskich grafik (cyfry, bomby, flagi).
* Interakcja: Obsługa zdarzeń myszy (LKM – otwieranie pól, PKM – flagowanie) oraz skrótów klawiszowych (F11 – tryb pełnoekranowy).
* Responsywność: Automatyczne dostosowanie rozmiaru okna i wielkości komórek (CELL_SIZE) do wybranego poziomu trudności.
* System komunikatów: Wyświetlanie nakładek wizualnych po wygranej lub przegranej rozgrywce.
-----------------------------------------
TWORZENIE ŚRODOWISKA WIRTUALNEGO:
Aby utworzyć środowisko wirtualne (venv) oraz zainstalować wszystkie wymagane biblioteki wymienione w pliku import_lib.txt, należy uruchomić plik create_venv.bat.

UWAGA:
Plik import_lib.txt jest obecnie pusty, ponieważ projekt nie wykorzystuje dodatkowych bibliotek. Został on jednak pozostawiony celowo, aby umożliwić ich dodanie w przyszłości (zgodnie z punktem 4).




