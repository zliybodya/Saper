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
W tej sekcji opisano backend gry, który zarządza stanem planszy i logiką rozgrywki.

* def matrix_generacia(rozmiar, r_first, c_first)
 Struktura danych: Tworzy macierz 3D, gdzie każda komórka to lista [wartość, stan].
   wartość: -1 (bomba), 0 (puste), 1-8 (liczba bomb w sąsiedztwie).
   stan: 0 (zakryte), 1 (odkryte), 2 (flaga).
 Mechanizm Safe-Start: Używając parametrów r_first i c_first, funkcja definiuje strefę bezpieczeństwa 3 na 3. Bomby nigdy nie zostaną wygenerowane na polu klikniętym jako pierwsze ani w jego bezpośrednim sąsiedztwie.
 Gęstość bomb: Automatycznie ustawiona na 20% powierzchni planszy.

* def open_cell(matrix, r, c)
Obsługuje interakcję odkrywania pola.
 Flood Fill: Jeśli odkryte pole ma wartość 0, funkcja rekurencyjnie otwiera wszystkich sąsiadów, aż napotka pola z liczbami.
 Zwracana wartość: False, jeśli gracz trafił na bombę, w przeciwnym razie True.

* def toggle_flag(matrix, r, c)
Zmienia stan pola między zakrytym (0) a flagą (2). Blokuje to możliwość przypadkowego odkrycia pola oznaczonego jako podejrzenie bomby.

* def check_win(matrix)
Przeszukuje planszę w celu sprawdzenia warunku zwycięstwa. Gracz wygrywa, gdy wszystkie pola niebędące bombami mają stan 1 (odkryte).

- logik.py:
* def toggle_flag(matrix, r, c)
 Cel: Zarządzanie oznaczeniami pól przez gracza.
 Działanie: Funkcja modyfikuje "stan" komórki (drugi element listy w macierzy).
 Logika:
~Jeśli pole jest zakryte (stan 0), zmienia go na flagę (stan 2).
~Jeśli na polu jest flaga (stan 2), zdejmuje ją, przywracając stan zakryty (stan 0).

* def open_cell(matrix, r, c)
 Cel: Odkrywanie zawartości pola oraz obsługa reakcji łańcuchowej.
 Walidacja: Sprawdza, czy współrzędne mieszczą się w granicach planszy i czy pole nie jest już odkryte lub oflagowane.
 Trafienie na minę: Jeśli wartość == -1, funkcja zwraca False, co kończy grę.
 Flood Fill (Algorytm zalewania): Jeśli gracz trafi na puste pole (wartość 0), funkcja rekurencyjnie wywołuje samą siebie dla wszystkich 8 sąsiednich pól. Dzięki temu jedno kliknięcie może odkryć duży obszar "bezpiecznych" pól.
 Wynik: Zwraca True, jeśli ruch był bezpieczny.

* def check_win(matrix)
 Cel: Weryfikacja, czy gra powinna się zakończyć sukcesem.
 Działanie: Przeszukuje całą macierz pole po polu.
 Warunek wygranej: Gra kończy się zwycięstwem tylko wtedy, gdy każde pole, które nie jest miną (cell[0] != -1), ma stan "otwarte" (cell[1] == 1).
 Logika: Jeśli znajdzie choć jedno bezpieczne pole, które wciąż jest zakryte, natychmiast przerywa sprawdzanie i zwraca False.

* def get_start_settings(level_name)
 Cel: Konfiguracja poziomu trudności.
 Działanie: Mapuje tekstową nazwę poziomu na konkretny rozmiar planszy.
 Dostępne poziomy: łatwy: 4x4; średni: 8x8; trudny: 16x16
 Bezpieczeństwo: Jeśli gracz wpisze nieznaną nazwę, domyślnie ustawiany jest poziom średni (8x8).

* def handle_end_game(user_choice, current_size)
 Cel: Zarządzanie przepływem aplikacji po zakończeniu partii.
 Działanie: Przetwarza decyzję gracza i decyduje o dalszym losie pętli gry.
 Opcje:
    Kontynuuj: Generuje nową planszę o tym samym rozmiarze.
    Zmien trudnosc: Zwraca sygnał do menu głównego w celu rekonfiguracji rozmiaru.
    Wyjdz: Wysyła sygnał zamknięcia aplikacji.


- grafic.py:
Ta część projektu odpowiada za renderowanie gry i interakcję z graczem za pomocą biblioteki tkinter.

* def reg() - System Renderowania
Jest to funkcja odświeżająca widok planszy.
 Mapowanie obrazów: Funkcja używa słownika images_map, aby przypisać wartościom liczbowym z macierzy odpowiednie pliki graficzne (np. 1.png, bomba.png).
 Dynamiczne rysowanie: Czyści Canvas i rysuje każdy kwadrat na nowo, sprawdzając jego stan:
     Jeśli stan == 2 -> rysuje flagę.
     Jeśli stan == 1 -> rysuje liczbę lub bombę.
     Jeśli stan == 0 -> rysuje pusty zakryty kwadrat.

* def lkm(event) (Lewy Przycisk Myszy): 
Przelicza współrzędne kliknięcia na indeksy macierzy.
 Obsługuje pierwszy ruch (generuje bomby po kliknięciu).
 Sprawdza przegraną (trafienie w bombę) lub wywołuje open_cell

* def rkm(event) (Prawy Przycisk Myszy): 
Wywołuje funkcję toggle_flag, pozwalając graczowi na oznaczanie min.

* def set_level(level_name)
Funkcja restartująca i konfigurująca nową grę.
Resetuje flagi zwycięstwa/przegranej (winche).
Pobiera nowy rozmiar planszy z get_start_settings.
Adaptacja GUI: Zmienia rozmiar Canvas i dostosowuje wielkość okna aplikacji do nowej liczby pól.
  Zarządzanie stanem gry:
     winche: Flaga globalna, która blokuje możliwość dalszych kliknięć po zakończeniu gry (wygranej lub przegranej).
     Overlay: Wykorzystuje widgety Label (win i prz), które są wyświetlane nad planszą za pomocą metody .lift() i .place(), informując o wyniku

-----------------------------------------
TWORZENIE ŚRODOWISKA WIRTUALNEGO:
Aby utworzyć środowisko wirtualne (venv) oraz zainstalować wszystkie wymagane biblioteki wymienione w pliku import_lib.txt, należy uruchomić plik create_venv.bat.

UWAGA:
Plik import_lib.txt jest obecnie pusty, ponieważ projekt nie wykorzystuje dodatkowych bibliotek. Został on jednak pozostawiony celowo, aby umożliwić ich dodanie w przyszłości (zgodnie z punktem 4).
