import sys

#region Configuration Port
CONFIGURATION_PORT: int = 4233
"""
Port for Communication with the configuration tool
"""
#endregion

#region Logging
LOG_FORMAT: str = '[%(asctime)s] [%(levelname)s] %(message)s at %(pathname)s, line %(lineno)d, Function: %(funcName)s'
"""
Format String for the logger. 

For available variables, see https://docs.python.org/3/library/logging.html#logrecord-attributes
"""
LOG_TO_CONSOLE: bool = True
"""
If True, logs to Stdout
"""
#endregion

#region Plugins
PLUGIN_DIRECTORY = ["../VirtualStudioPlugins", "../libwsctrl", "../OBSWebsocketPlugin", "../DMXPlugin", "../systemfunctionsplugin"]
"""
List of directories containing all plugins and libaries. Before a plugin, all libaries should be listed
"""
#endregion

#region Data
ACCOUNT_DATA_DIRECTORY = "../r3s-config-data/data/account"
"""
Direcotry containing profile data
"""

ACCOUNT_DATA_FILE = "accounts.json"
"""
Serialised ProfileSets
"""

PROFILE_DATA_DIRECTORY = "../r3s-config-data/data/vscore1/profile"
"""
Direcotry containing profile data
"""

PROFILE_SET_DATA_FILE = "profilesets.json" #"emptyset.json" #
"""
Serialised ProfileSets
"""

DEVICE_CURRENT_PROFILE_NAME = "profilenames.json"
"""
Current Profile Name per device
"""

#endregion

#region Native Libray search paths
NATIVE_LIBRARY_PATH_HIDAPI = sys.path[0] + "\\native\\hidapi.dll"
"""
Path to native HIDAPI library. If the file specified is not valid, the system is searched for an installed version in
the usual places.
"""
#endregion