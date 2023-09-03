# Import necessary libraries
from pathlib import Path
import shutil
import configparser
import sys

config = configparser.ConfigParser()

# Determine the path to the bundled configuration file
if getattr(sys, "frozen", False):
    # Running as a standalone executable
    base_path = Path(sys.executable).parent
else:
    # Running as a standard .py file
    base_path = Path(__file__).parent

# The location of the example config
conf = base_path / "brswitch.conf"

# The user's home directory
home = Path.home()
# The location where the user config should be: ~/brswitch.conf
brs_userconf = home / "brswitch.conf"


# Initiate the configuration
def brs_initconf():
    # If the config file exists, do nothing
    if brs_userconf.is_file():
        print(f"Configurator: The file {brs_userconf} exists.")
    # If the config file doesn't exist, copy the default one to the home directory
    else:
        print(
            f"The file {brs_userconf} does not exist. Copying default configuration to the home folder."
        )
        shutil.copy(conf, brs_userconf)


# Reset last switched branch value in the config
def brs_resetconf():
    # Load the configuration file
    config.read(brs_userconf)
    # Clear the value for last_branch
    config["history"]["last_branch"] = ""
    # Write the changes back to the configuration file
    with open(brs_userconf, "w") as config_file:
        config.write(config_file)
    print("Branch reset successfully.")


# Write last switched branch value in the config
def brs_writelast(branch):
    # Load the configuration file
    config.read(brs_userconf)
    # Write the value for the last branch using the information from the switcher
    config["history"]["last_branch"] = branch
    # Write the changes back to the configuration file
    with open(brs_userconf, "w") as config_file:
        config.write(config_file)
    print("Branch switched successfully.")
