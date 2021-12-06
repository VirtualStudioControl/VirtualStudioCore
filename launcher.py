import sys

STREAMDECK_LIBRARY_PATH = "../python-elgato-streamdeck/src"
LIBMIDICTRL_LIBRARY_PATH = "../libmidictrl"
VIRTUAL_STUDIO_COMMON_PATH = "../virtualstudio_common"


sys.path.append(STREAMDECK_LIBRARY_PATH)
sys.path.append(LIBMIDICTRL_LIBRARY_PATH)
sys.path.append(VIRTUAL_STUDIO_COMMON_PATH)

import main

main.run()