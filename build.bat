@echo off

del /F /S *.exe

set "lj=%~p0"
set "lj=%lj:\= %"
for %%a in (%lj%) do set wjj=%%a
pyinstaller --onefile --icon=icon.ico %wjj%.py

rd /s /q __pycache__
rd /s /q build
move dist\*.exe %cd%\
rd /s /q dist
del /F /S *.spec