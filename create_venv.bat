@echo off
REM Sprawdzenie, czy Python jest zainstalowany
python --version >nul 2>&1
if errorlevel 1 (
    echo Python nie zostal znaleziony. Zainstaluj Pythona i dodaj go do PATH.
    pause
    exit /b
)

REM Tworzenie wirtualnego srodowiska
if not exist venv (
    echo Tworzenie wirtualnego srodowiska...
    python -m venv venv
) else (
    echo Wirtualne srodowisko venv juz istnieje.
)

REM Aktywacja wirtualnego srodowiska
call venv\Scripts\activate

REM Aktualizacja pip
python -m pip install --upgrade pip

REM Instalacja bibliotek z pliku import_lib.txt
if exist import_lib.txt (
    pip install -r import_lib.txt
) else (
    echo Plik import_lib.txt nie zostal znaleziony!
)

echo.
echo Gotowe
pause
