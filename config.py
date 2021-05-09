import sys

#region Configuration Port
CONFIGURATION_PORT = 4233
"""
Port for Communication with the configuration tool
"""
#endregion

#region Plugins
PLUGIN_DIRECTORY = "B:/Repositorys/ChaosStudio/VirtualStudioPlugins"
"""
Directory containing all cross-platform plugins
"""
PLUGIN_DIRECTORY_PLATFORM = ""
"""
Directory containing all platform specific plugins
"""
#endregion

#region Data
PROFILE_DATA_DIRECTORY = ""
"""
Direcotry containing profile data
"""
#endregion

#region Native Libray search paths
NATIVE_LIBRARY_PATH_HIDAPI = sys.path[0] + "\\native\\hidapi.dll"
"""
Path to native HIDAPI library. If the file specified is not valid, the system is searched for an installed version in
the usual places.
"""
#endregion