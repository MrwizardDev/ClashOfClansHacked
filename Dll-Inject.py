import ctypes
import time

# Load the Clash of Clans DLL
clash_dll = ctypes.WinDLL("libClashOfClans.dll")

# Find the address of the function that sets the resource count
set_resource_count_func = clash_dll.SetResourceCount
set_resource_count_func.argtypes = [ctypes.c_int, ctypes.c_int]

# Set the resource count to a large value (e.g., 1 million)
set_resource_count_func(1000000, 1000000)

# Keep the script running to prevent the game from closing
while True:
    time.sleep(1)
