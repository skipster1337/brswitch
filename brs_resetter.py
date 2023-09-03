import glob
from pathlib import Path

# Load the config path from the configurator, the branch config resetter, and the config variable used for interacting with configparser
from brs_configurator import brs_userconf, brs_resetconf, config


# TODO: also check for broken manifests in future versions for more edge cases
# For now this is just a basic working version


# Reset branches before proceeding with operations
def brs_reset():
    # Open the config file
    config.read(brs_userconf)
    # Read game path from config
    game_path = config["paths"]["game_path"]
    # Convert game_path string to Path object
    brs_game_path = Path(game_path)
    # Get the path for the "Brick Rigs" folder itself
    brpath = brs_game_path / "Brick Rigs"
    # Read last switched branch from history
    last_branch = config["history"]["last_branch"]
    # If last branch is unknown, check for modified folder structure to avoid problems
    if last_branch == "":
        # Search for modified folder names in the game path using glob
        matching_modified = glob.glob(str(brs_game_path / "br_*"))
        # If modified files are found
        if matching_modified:
            # Also check for "Brick Rigs" folder which indicates that branches were switched at some point, which means your brswitch is FUBAR'd
            # If no "Brick Rigs" folder is found, it should mean that the branches don't need resetting (each branch is properly codenamed) and it will let you pass
            if brpath.is_dir():
                # Bad ending: Modified structure found, active branch found of unknown type
                print(
                    "The last switched branch is unknown, a modified folder structure was found, and an unknown currently active branch was also found. Sorry, but your brswitch install might be broken. Refer to the GitHub page for more info."
                )
                input("Press Enter to exit.")
                exit()
        # If modified files are not found
        else:
            print(
                "The last switched branch is unknown, and a modified folder structure was not found. This usually means that you haven't set up your brswitch folder structure yet."
            )
            input("Press Enter to continue.")
    # Last switched branch in config is not empty
    else:
        # Check for "Brick Rigs" folder in the game path
        # If "Brick Rigs" folder is found, proceed with resetting
        if brpath.is_dir():
            print(
                f"\nActive branch is {last_branch}. Resetting selected branch before switching."
            )
            # Get location of active BR folder
            old_br_path = brs_game_path / "Brick Rigs"
            # Get the path to the new folder
            new_br_path = brs_game_path / f"br_{last_branch}"
            # Rename active branch to its respective codename
            old_br_path.rename(new_br_path)
            # Also rename .acf files
            # Go up one level to the .acf file location
            appmanifest_location = brs_game_path.parent
            # Get the path to the old appmanifest
            old_appmanifest_path = appmanifest_location / "appmanifest_552100.acf"
            # Get the path to the new appmanifest
            new_appmanifest_path = appmanifest_location / f"br_{last_branch}.acf"
            # Rename active appmanifest to its respective codename
            old_appmanifest_path.rename(new_appmanifest_path)
            # Reset active branch value in the config
            brs_resetconf()
        else:
            # If active branch is found in config, but no "Brick Rigs" folder is found, bail out
            print(
                f"The last switched branch found in the config is {last_branch}, but no active branch folder was found in the game path. Sorry, but your brswitch install might be broken. Refer to the GitHub page for more info."
            )
            input("Press Enter to exit.")
            exit()
