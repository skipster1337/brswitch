from pathlib import Path
import glob

# Load the game path variables and the branch config resetter.
from brsConfig import brsConfig_ReadLastBranch, brsConfig_ReadGameLocation, brsConfig_ResetConf


# TODO: also check for broken manifests in future versions for more edge cases
# For now this is just a basic working version


# Reset branches before proceeding with operations
brsConfig_LastBranch = brsConfig_ReadLastBranch()
brsConfig_GameLocation, brsConfig_GamePath = brsConfig_ReadGameLocation()
def brsReset():
    # If last branch is unknown, check for modified folder structure to avoid problems
    if brsConfig_LastBranch == "":
        # Search for modified folder names in the game path using glob
        matching_modified = glob.glob(str(brsConfig_GameLocation / "br_*"))
        # If modified files are found
        if matching_modified:
            # Also check for "Brick Rigs" folder which indicates that branches were switched at some point, which means your brswitch is FUBAR'd
            # If no "Brick Rigs" folder is found, it should mean that the branches don't need resetting (each branch is properly codenamed) and it will let you pass
            if brsConfig_GamePath.is_dir():
                # Bad ending: Modified structure found, active branch found of unknown type
                print(
                    "\nThe last switched branch is unknown, a modified folder structure was found, and an unknown currently active branch was also found. Sorry, but your brswitch install might be broken. Refer to the GitHub page for more info."
                )
                input("Press Enter to exit.")
                exit()
        # If modified files are not found
        else:
            print(
                "\nThe last switched branch is unknown, and a modified folder structure was not found. This usually means that you haven't set up your brswitch folder structure yet."
            )
            input("Press Enter to exit.")
            exit()
    # If last switched branch in config is not empty
    else:
        # Check for "Brick Rigs" folder in the game path
        # If "Brick Rigs" folder is found, proceed with resetting
        if brsConfig_GamePath.is_dir():
            print(
                f"\nActive branch is {brsConfig_LastBranch}. Resetting selected branch before switching."
            )
            # Get location of active BR folder
            old_br_path = brsConfig_GamePath
            # Get the path to the new folder
            new_br_path = brsConfig_GameLocation / f"br_{brsConfig_LastBranch}"
            # Rename active branch to its respective codename
            old_br_path.rename(new_br_path)
            # Also rename .acf files
            # Go up one level to the .acf file location
            appmanifest_location = brsConfig_GameLocation.parent
            # Get the path to the old appmanifest
            old_appmanifest_path = appmanifest_location / "appmanifest_552100.acf"
            # Get the path to the new appmanifest
            new_appmanifest_path = appmanifest_location / f"br_{brsConfig_LastBranch}.acf"
            # Rename active appmanifest to its respective codename
            old_appmanifest_path.rename(new_appmanifest_path)
            # Reset active branch value in the config
            brsConfig_ResetConf()
        else:
            # If active branch is found in config, but no "Brick Rigs" folder is found, bail out
            print(
                f"\nThe last switched branch found in the config is {brsConfig_LastBranch}, but no active branch folder was found in the game path. Sorry, but your brswitch install might be broken. Refer to the GitHub page for more info."
            )
            input("Press Enter to exit.")
            exit()
