@echo off
echo Payload build script.
pause
pip install pyinstaller
pyinstaller -F payload/payload.py
echo Check dist folder for the executable file.
