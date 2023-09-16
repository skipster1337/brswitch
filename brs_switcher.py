from pathlib import Path
from brs_configurator import brs_writelast, brs_userconf, config


# Branch switcher function
# Get branch name from selected menu option
def brs_switcher(branch):
    print(f"\nSwitching to {branch}.")
    # Open the config file
    config.read(brs_userconf)
    # Read game path from config file
    game_path = config["paths"]["game_path"]
    # Convert game_path string to Path object
    brs_game_path = Path(game_path)
    # Use the obtained branch name to figure out which BR folder to switch
    old_br_folder = f"br_{branch}"
    # Append branch name for full path
    old_br_path = brs_game_path / old_br_folder
    # Check if required BR path exists
    if old_br_path.is_dir():
        # Rename needed branch to "Brick Rigs"
        print(f'Renaming {old_br_folder} to "Brick Rigs"')
        # Get path of new BR folder by appending new folder name to base path
        new_br_path = brs_game_path / "Brick Rigs"
        # Rename folders using obtained path variables
        old_br_path.rename(new_br_path)
        # Go up to steamapps folder for appmanifest location
        appmanifest_location = brs_game_path.parent
        # Append branch name for full appmanifest path
        old_appmanifest_path = appmanifest_location / f"br_{branch}.acf"
        # Append new appmanifest name for full path
        new_appmanifest_path = appmanifest_location / "appmanifest_552100.acf"
        # Rename files using obtained path variables
        old_appmanifest_path.rename(new_appmanifest_path)
        # Change last switched branch value in the config
        brs_writelast(branch)
        # No need to check for other broken stuff yet since it passed through the resetter
        # Will probably still do it in the future anyway to cover edge cases
    else:
        # If required branch is not found, bail out
        print(
            f"{old_br_folder} does not exist! Have you set up your branches correctly?"
        )
