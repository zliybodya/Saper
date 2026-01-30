@echo off
chcp 65001 > nul
echo   Konfiguracja środowiska projektu
set /p choice="Czy chcesz utworzyć środowisko wirtualne (venv) i zainstalować pakiety? (y/n): "

if /i "%choice%"=="y" (
    if exist import_lib.txt (
        pip install -r import_lib.txt
    ) else (
        echo Brak pliku import_lib.txt
    )
    echo Gotowe!
    pause
) else (
    echo Przerwano konfigurację.
    pause
)
