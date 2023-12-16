# Import necessary libraries
from pathlib import Path
import shutil
import configparser
import sys

config = configparser.ConfigParser()


# Determine the path to the bundled configuration file
if getattr(sys, "frozen", False):
    # Running as a standalone executable
    base_path = Path(sys._MEIPASS)  # type: ignore
else:
    # Running as a standard .py file
    base_path = Path(__file__).parent


# The location of the example config
conf = base_path / "brswitch.conf"
# The user's home directory
home = Path.home()
# The location where the user config should be: ~/brswitch.conf
brsConfig_UserConf = home / "brswitch.conf"


def brsConfig_InitConf():
    # Initiate the configuration
    # If the config file exists, do nothing
    if brsConfig_UserConf.is_file():
        print(f"Configuration: The file {brsConfig_UserConf} exists.")
    # If the config file doesn't exist, copy the default one to the home directory
    else:
        print(
            f"The file {brsConfig_UserConf} does not exist. Copying default configuration to the home folder."
        )
        shutil.copy(conf, brsConfig_UserConf)


# Reset last switched branch value in the config
def brsConfig_ResetConf():
    # Load the configuration file
    config.read(brsConfig_UserConf)
    # Clear the value for last_branch
    config["history"]["last_branch"] = ""
    # Write the changes back to the configuration file
    with open(brsConfig_UserConf, "w") as config_file:
        config.write(config_file)
    print("Branch reset successfully.")


# Write last switched branch value in the config
def brsConfig_WriteLastBranch(branch):
    # Load the configuration file
    config.read(brsConfig_UserConf)
    # Write the value for the last branch using the information from the switcher
    config["history"]["last_branch"] = branch
    # Write the changes back to the configuration file
    with open(brsConfig_UserConf, "w") as config_file:
        config.write(config_file)
    print("Branch switched successfully.")


# Read last switched branch from config file
def brsConfig_ReadLastBranch():
    # Load the configuration file
    config.read(brsConfig_UserConf)
    # Read last switched branch from history
    brsConfig_LastBranch = config["history"]["last_branch"]
    # Return the variable
    return brsConfig_LastBranch


# Read Steam location from config file
def brsConfig_ReadSteamLocation():
    # Load the configuration file
    config.read(brsConfig_UserConf)
    # Read Steam location from config
    steam_location = config["paths"]["steam_location"]
    # Convert steam_location string to Path object
    brsConfig_SteamLocation = Path(steam_location)
    # Get the location of the Steam executable
    brsConfig_SteamExe = brsConfig_SteamLocation / "steam.exe"
    # Return the variables
    return brsConfig_SteamLocation, brsConfig_SteamExe


# Read game location from config file
def brsConfig_ReadGameLocation():
    # Load the configuration file
    config.read(brsConfig_UserConf)
    # Read game location from config
    game_location = config["paths"]["game_location"]
    # Convert game_location string to Path object
    brsConfig_GameLocation = Path(game_location)
    # Get the path for the "Brick Rigs" folder itself
    brsConfig_GamePath = brsConfig_GameLocation / "Brick Rigs"
    # Return the variables
    return brsConfig_GameLocation, brsConfig_GamePath
