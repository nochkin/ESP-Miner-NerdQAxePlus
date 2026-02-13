"""
PlatformIO build script to set BOARD environment variable based on build environment
"""
import os

Import("env")

# Get the current environment name from PlatformIO
current_env = env["PIOENV"]

# Map environment names to BOARD values
board_mapping = {
    "nerdqaxeplus2": "NERDQAXEPLUS2",
    "nerdqaxeplus": "NERDQAXEPLUS",
    "nerdoctaxeplus": "NERDOCTAXEPLUS",
    "nerdoctaxegamma": "NERDOCTAXEGAMMA",
    "nerdhaxegamma": "NERDHAXEGAMMA",
    "nerdaxegamma": "NERDAXEGAMMA",
    "nerdaxe": "NERDAXE",
    "nerdqx": "NERDQX",
    "nerdeko": "NERDEKO",
}

# Set the BOARD environment variable
if current_env in board_mapping:
    board_value = board_mapping[current_env]
    env["ENV"]["BOARD"] = board_value
    print(f"Setting BOARD environment variable to: {board_value}")
else:
    print(f"Warning: Unknown environment '{current_env}', BOARD not set")
