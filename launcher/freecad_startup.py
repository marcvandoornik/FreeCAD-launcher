import os
mp = os.environ['FREECAD_MACRO_DIR']
mp = mp.replace('\\', '/')

App.ParamGet('User parameter:BaseApp/Preferences/Macro').SetString('MacroPath', mp)
