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

command = config.FREECAD_DIR+'/bin/freecad.exe'
command += ' -l'
command += ' --set-config ExeName=' + '"' + config.EXE_NAME + '"'
command += ' --set-config AppIcon=' + cwd + '/' + config.BRANDING_DIR + '/freecad.ico'
command += ' --set-config SplashScreen=' + cwd + '/' + config.BRANDING_DIR + '/SplashScreen.png'
command += ' --set-config ProgramIcons=' + cwd + '/' + config.BRANDING_DIR + '/freecad.ico'
command += ' --set-config ProgramLogo=' + cwd + '/' + config.BRANDING_DIR + '/freecad.ico'

subprocess.run(command, env = env)




