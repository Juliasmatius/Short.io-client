@echo off
del "URL shortener.exe"
python -m PyInstaller --windowed --onefile main.py --name "URL shortener"
move "%cd%\dist\URL shortener.exe" .