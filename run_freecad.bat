@echo off
cls

REM ============================================================================
REM SET THIS TO THE FREECAD INSTALLATION DIRECTORY
REM ============================================================================

set FREECAD_DIR=c:\marc_portable\bin\freecad


REM ============================================================================
REM DO NOT CHANGE BELOW THIS LINE
REM ============================================================================

if not exist %~dp0python\Scripts\python.exe ( 
  echo Local Python does not exist. Creating virtual environment.
  %FREECAD_DIR%\bin\python.exe -m venv %~dp0python
)

echo Starting FreeCAD.
echo %~dp0python\Scripts\python.exe %~dp0run_freecad.py 
%~dp0python\Scripts\python.exe %~dp0run_freecad.py 
