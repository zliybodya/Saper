@echo off
REM Sprawdzenie, czy wirtualne srodowisko istnieje
if not exist venv\Scripts\activate.bat (
    echo Wirtualne srodowisko venv nie istnieje.
    echo Najpierw uruchom setup_venv.bat
    pause
    exit /b
)

REM Aktywacja wirtualnego srodowiska
call venv\Scripts\activate

REM Sprawdzenie, czy plik grafic.py istnieje
if not exist grafic.py (
    echo Plik grafic.py nie zostal znaleziony!
    pause
    exit /b
)

REM Uruchomienie skryptu Python
python grafic.py

pause


