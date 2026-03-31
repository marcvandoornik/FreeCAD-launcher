# ============================================================================
# SETTINGS FOR THIS FREECAD INSTANCE
# ============================================================================

import os
import subprocess
import re
import time
import config


# ============================================================================
# COLOR PRINTING FUNCTIONS
# ============================================================================

def prRed(s): print("\033[91m {}\033[00m".format(s))
def prGreen(s): print("\033[92m {}\033[00m".format(s))
def prYellow(s): print("\033[93m {}\033[00m".format(s))
def prLightPurple(s): print("\033[94m {}\033[00m".format(s))
def prPurple(s): print("\033[95m {}\033[00m".format(s))
def prCyan(s): print("\033[96m {}\033[00m".format(s))
def prLightGray(s): print("\033[97m {}\033[00m".format(s))
def prBlack(s): print("\033[90m {}\033[00m".format(s))  # Corrected from 98 to 90 (standard ANSI)

def prLeft(s): print(f'{s:<70}', end='')
def prRightGreen(s): prGreen(f'{s:<10}')
def prRightRed(s): prRed(f'{s:<10}')


# ============================================================================
# PRINT A NICE LITTLE HEADER
# ============================================================================

os.system('clear')
STR = 'FREECAD PORTABLE PYTHON LAUNCHER'
BRD = '='
CHAR = ' '
WIDTH = 80
print(f'{BRD:=^{WIDTH}}')
print(f'{STR:{CHAR}^{WIDTH}}')
print(f'{BRD:=^{WIDTH}}')
print()


# ============================================================================
# CHECK IF GIT IS INSTALLED IN THE PATH
# ============================================================================

prLeft('Checking if Git is installed in the path...')
try:
    subprocess.call(['git', '--version'], stdout=subprocess.DEVNULL)
    git_found = True
    prRightGreen('Ok.')
except:
    git_found = False
    prRightRed('Not found.')
    print('Git was not found in the path; please install Git and retry.')
    print()
    input('Press ENTER to exit.')
    exit()


# ============================================================================
# ASSIGN ENVIRONMENT VARIABLES
# ============================================================================

cwd = os.path.normpath(os.getcwd()).replace(os.sep, '/')
FREECAD_DIR = os.path.normpath(os.environ['FREECAD_DIR'])
PYTHONPATH  = config.PYTHONPATH

env =  {'BRANDING_DIR'      : cwd + '/' + config.BRANDING_DIR}
env |= {'FREECAD_USER_HOME' : cwd + '/' + config.FREECAD_USER_HOME}
env |= {'FREECAD_USER_TEMP' : cwd + '/' + config.FREECAD_USER_TEMP}
env |= {'FREECAD_MACRO_DIR' : cwd + '/' + config.FREECAD_MACRO_DIR}
env |= {'PYTHONPATH'        : cwd + '/' + config.PYTHONPATH}

env |= {'QT_QPA_PLATFORM' : config.QT_QPA_PLATFORM}


# ============================================================================
# ADD SCRIPTS DIR TO PATH
# ============================================================================

# env['PATH'] = os.environ['FREECAD_DIR']+'/bin/Scripts'+';'+os.environ['PATH']
env['PATH'] = FREECAD_DIR+'/bin/Scripts'+';'+os.environ['PATH']
env['PATH'] = PYTHONPATH+'/Scripts'+';'+os.environ['PATH']


# Assume first run if data directory does not exist.
# If this is the case, create data directory

prLeft('Checking if the data directory exists...')

if not os.path.exists('data'):
    prRightRed('Not found.')
    prLeft('Creating data directory...')
    os.makedirs('data/Mod')
    prRightGreen('Done.')

    # Upgrade pip
    print()
    print('============================================================')
    print('Upgrading pip...')
    print('============================================================')
    print()
    time.sleep(1)
    subprocess.run(cwd + '/' + PYTHONPATH + '/Scripts/python.exe -m pip install --upgrade pip')
    print()
    print('============================================================')
    prGreen('Done.')
    print('============================================================')
    print()

    # Install Netgen and Numpy
    print('============================================================')
    print('Installing Netgen and Numpy...')
    print('============================================================')
    print()
    time.sleep(1)
    subprocess.run(cwd + '/' + PYTHONPATH + '/Scripts/pip.exe install ngsolve numpy')
    print()
    print('============================================================')
    prRightGreen('Done.')
    print('============================================================')
else:
    prRightGreen('Found.')

os.chdir('data/Mod')

# Install all addons from config.py
print('\nChecking for configured addons:')

for ADDON in config.ADDONS:
    DIR = re.search(r'[^/]+$', ADDON).group()
    prLeft('    Checking addon ' + DIR + '...')
    if not os.path.exists(DIR):
        prRightRed('Not found.')
        prLeft('    ... Installing from ' + ADDON + '...')
        subprocess.run('git clone ' + ADDON)
        prRightGreen('Done.')
    else:
        prRightGreen('Exists.')


# For now, try to fire up FreeCAD:

env |= os.environ

command = FREECAD_DIR+'/bin/freecad.exe'
command += ' -l'
command += ' --set-config ExeName=' + '"' + config.EXE_NAME + '"'
command += ' --set-config AppIcon=' + cwd + '/' + config.BRANDING_DIR + '/freecad.ico'
command += ' --set-config SplashScreen=' + cwd + '/' + config.BRANDING_DIR + '/SplashScreen.png'
command += ' --set-config ProgramIcons=' + cwd + '/' + config.BRANDING_DIR + '/freecad.ico'
command += ' --set-config ProgramLogo=' + cwd + '/' + config.BRANDING_DIR + '/freecad.ico'

subprocess.run(command, env = env)




