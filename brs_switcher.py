from brs_resetter import brs_game_path
from brs_configurator import brs_writelast

# TODO: i have to comment this abomination better

# Branch switcher function
def brs_switcher(branch):
    print(f"\nSwitching to {branch}.")
    # Check if required branch folder exists
    old_br_folder = f"br_{branch}"
    old_br_path = brs_game_path / old_br_folder
    if old_br_path:
        print(f"{old_br_folder} exists!")
    # Rename needed branch to "Brick Rigs"
    print(f'Renaming {old_br_folder} to "Brick Rigs"')
    new_br_path = brs_game_path / "Brick Rigs"
    old_br_path.rename(new_br_path)
    # Go up a folder and rename appmanifest to "appmanifest_552100.acf"
    appmanifest_location = brs_game_path.parent
    old_appmanifest_path = appmanifest_location / f"br_{branch}.acf"
    new_appmanifest_path = appmanifest_location / "appmanifest_552100.acf"
    old_appmanifest_path.rename(new_appmanifest_path)
    # Change last switched branch value in the config
    brs_writelast(branch)
    # No need to check for other broken stuff yet since it passed through the resetter
    # Will probably still do it in the future anyway to cover edge cases
