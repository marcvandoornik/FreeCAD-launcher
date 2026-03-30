# ============================================================================
# SETTINGS FOR THIS FREECAD INSTANCE
# ============================================================================

import os
import subprocess
import config

cwd = os.path.normpath(os.getcwd()).replace(os.sep, '/')

env =  {'BRANDING_DIR'      : cwd + '/' + config.BRANDING_DIR}
env |= {'FREECAD_USER_HOME' : cwd + '/' + config.FREECAD_USER_HOME}
env |= {'FREECAD_USER_TEMP' : cwd + '/' + config.FREECAD_USER_TEMP}
env |= {'FREECAD_MACRO_DIR' : cwd + '/' + config.FREECAD_MACRO_DIR}
env |= {'PYTHONPATH'        : cwd + '/' + config.PYTHONPATH}

env |= {'QT_QPA_PLATFORM' : config.QT_QPA_PLATFORM}


# ============================================================================
# ADD SCRIPTS DIR TO PATH
# ============================================================================

env['PATH'] = config.FREECAD_DIR+'/bin/Scripts'+';'+os.environ['PATH']


# Check if first run
# If so: install OpenTheme, ngsolve and numpy

# For now, try to fire up FreeCAD:
# ================================

# subprocess.Popen(cwd+'/speak.bat', env=myenv) 
# subprocess.Popen('c:\\marc_portable\\data\\freecad\\freecad_python_launcher_test\\speak.bat', env = env)

env |= os.environ
arguments = [
    '-l', 
    '--set-config', 'ExeName=' + config.EXE_NAME,
    '--set-config', 'AppIcon=' + config.BRANDING_DIR + '/freecad.ico', 
    '--set-config', 'SplashScreen=' + config.BRANDING_DIR + '/SplashScreen.png',
    '--set-config', 'ProgramIcons=' + config.BRANDING_DIR + '/freecad.ico',
    '--set-config', 'ProgramLogo=' + config.BRANDING_DIR + '/freecad.ico'
]

print(arguments)

# subprocess.run([config.FREECAD_DIR+'/bin/freecad.exe', '--set-config', 'ExeName=Greatest Goat Cheese Of All Time', '--set-config', 'ExeVersion=1.2.3'], env = env)

subprocess.run([config.FREECAD_DIR+'/bin/freecad.exe'] + arguments, env = env)




