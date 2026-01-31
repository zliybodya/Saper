@echo off
chcp 65001 > nul
echo Uruchamianie projektu

if not exist venv (
    echo Brak srodowiska wirtualnego (venv).
    echo Najpierw uruchom plik konfiguracyjny.
    pause
    exit /b
)

echo Aktywacja srodowiska wirtualnego...
call venv\Scripts\activate

echo Uruchamianie pliku grafic.py...
python grafic.py

echo Zakonczono dzialanie programu.
pause
