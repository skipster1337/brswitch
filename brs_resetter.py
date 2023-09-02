import glob
from pathlib import Path
from brs_configurator import brs_userconf, brs_resetconf, config

# Read game paths from config
config.read(brs_userconf)
game_path = config["paths"]["game_path"]
# Convert game_path string to Path object
brs_game_path = Path(game_path)


# Reset branches before proceeding with operations
def brs_reset():
    # Read last switched branch from config
    last_branch = config["history"]["last_branch"]
    # If last branch is unknown, check for modified folder structure to avoid problems
    if last_branch == "":
        # Search for modified folder names in the game path using glob
        matching_modified = glob.glob(str(brs_game_path / "br_*"))
        # If modified files are found
        if matching_modified:
            # Also check for "Brick Rigs" folder which indicates that branches were switched at some point, which means your brswitch is FUBAR'd
            brfolder = "Brick Rigs"
            fubar = brs_game_path / brfolder
            # Bad ending: Modified structure found, active branch found of unknown type
            if fubar.is_dir():
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
    # Last switched branch in config is not empty which means things *should* be good, proceed with resetting
    # TODO: If there is an active branch in the config but no Brick Rigs folder found in the files, don't do anything and let the user know
    # TODO: Also rename appmanifest files, otherwise this is useless.
    else:
        print(
            f"Active branch is {last_branch}. Resetting selected branch before switching."
        )
        # Get path for active BR folder
        old_br_path = brs_game_path / "Brick Rigs"
        # Get the name of the required folder from the config
        new_br_folder = "br_" + last_branch
        # Get the path with the new folder
        new_br_path = brs_game_path / new_br_folder
        # Rename active branch to its respective codename
        old_br_path.rename(new_br_path)
        # Reset active branch value in the config
        brs_resetconf()
