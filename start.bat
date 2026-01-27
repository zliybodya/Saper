@echo off
cls

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Błąd nie masz pythona
    pause
    exit
)

start "" pythonw grafic.py

exit