from pathlib import Path
from brsConfig import brsConfig_ReadGameLocation, brsConfig_WriteLastBranch


# Branch switcher function
# Get branch name from selected menu option
def brsSwitch(branch):
    print(f"\nSwitching to {branch}.")
    # Read game path from config file
    brsConfig_GameLocation, brsConfig_GamePath = brsConfig_ReadGameLocation()
    # Use the obtained branch name to figure out which BR folder to switch
    old_br_folder = f"br_{branch}"
    # Append branch name for full path
    old_br_path = brsConfig_GameLocation / old_br_folder
    # Check if required BR path exists
    if old_br_path.is_dir():
        # Rename needed branch to "Brick Rigs"
        print(f'Renaming {old_br_folder} to "Brick Rigs"')
        # Get path of new BR folder from config
        new_br_path = brsConfig_GamePath
        # Rename folders using obtained path variables
        old_br_path.rename(new_br_path)
        # Go up to steamapps folder for appmanifest location
        appmanifest_location = brsConfig_GameLocation.parent
        # Append branch name for full appmanifest path
        old_appmanifest_path = appmanifest_location / f"br_{branch}.acf"
        # Append new appmanifest name for full path
        new_appmanifest_path = appmanifest_location / "appmanifest_552100.acf"
        # Rename files using obtained path variables
        old_appmanifest_path.rename(new_appmanifest_path)
        # Change last switched branch value in the config
        brsConfig_WriteLastBranch(branch)
        # No need to check for other broken stuff yet since it passed through the resetter
        # Will probably still do it in the future anyway to cover edge cases
    else:
        # If required branch is not found, bail out
        print(
            f"{old_br_folder} does not exist! Have you set up your branches correctly?"
        )
