import sys

#region Configuration Port
CONFIGURATION_PORT = 4233
"""
Port for Communication with the configuration tool
"""
#endregion

#region Plugins
PLUGIN_DIRECTORY = "../VirtualStudioPlugins"
"""
Directory containing all cross-platform plugins
"""
PLUGIN_DIRECTORY_PLATFORM = ""
"""
Directory containing all platform specific plugins
"""
#endregion

#region Data
ACCOUNT_DATA_DIRECTORY = "./data/account"
"""
Direcotry containing profile data
"""

ACCOUNT_DATA_FILE = "accounts.json"
"""
Serialised ProfileSets
"""

PROFILE_DATA_DIRECTORY = "./data/profile"
"""
Direcotry containing profile data
"""

PROFILE_SET_DATA_FILE = "profilesets.json"
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