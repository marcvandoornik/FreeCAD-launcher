@echo off

REM ============================================================================
REM SETTINGS FOR THIS FREECAD INSTANCE
REM ============================================================================

REM The name of the FreeCAD installation directory under %BIN_DIR%
set FREECAD_DIR=freecad_weekly

REM Name for the program title bar
set EXE_NAME="FreeCAD TESTING WEEKLY"

REM Directory containing the custom images
set BRANDING_DIR=%~dp0launcher


REM ============================================================================
REM SET UP NECESSARY ENVIRONMENT VARIABLES
REM ============================================================================

set QT_QPA_PLATFORM=windows:darkmode=2

set FREECAD_USER_HOME=%~dp0data
set FREECAD_USER_TEMP=%~dp0temp
set FREECAD_MACRO_DIR=%~dp0macros
set PYTHONHOME=%~dp0python


REM ============================================================================
REM ADD SCRIPTS DIR TO PATH
REM ============================================================================

set PATH=%BIN_DIR%\%FREECAD_DIR%\bin\Scripts;%PATH%


REM ============================================================================
REM LAUNCH FREECAD
REM ============================================================================

start %BIN_DIR%\%FREECAD_DIR%\bin\Scripts\pip install --user ngsolve numpy
