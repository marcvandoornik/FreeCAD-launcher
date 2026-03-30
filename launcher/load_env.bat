@echo off

REM ============================================================================
REM LOAD ENVIRONMENT VARIABLES FROM FILE
REM ============================================================================

echo Loading environment variables from %~dp0..\env.txt
for /F "tokens=* eol=#" %%i in ('type %~dp0..\env.txt') do (
	call set %%i
)


REM ============================================================================
REM INITIALIZE ADDITIONAL PACKAGES AND ADDONS ON FIRST RUN
REM ============================================================================

if exist ..\first_run (
	cls
	echo First run; setting up the environment.
	pause

	cd ..
	echo Creating virtual environment for Python in %CD%
	echo start %BIN_DIR%\%FREECAD_DIR%\bin\python.exe -m venv python
	pause

        echo Installing Netgen and Numpy.
	echo start %BIN_DIR%\%FREECAD_DIR%\bin\Scripts\pip install --user ngsolve numpy
	pause

	cd data\Mod
	echo Installing OpenTheme to %CD%
	pause
	
	cd ..\..
	echo Renaming first_run to NOT_first_run
	ren ..\first_run NOT_first_run
)

echo ========================================
echo Current directory: %~dp0
echo LOADING FREECAD
echo ========================================

pause
