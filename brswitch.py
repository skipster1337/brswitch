from brsProcess import brsProcess_System, brsProcess_Kill
from brsConfig import brsConfig_InitConf
from brsReset import brsReset
from brsSwitcher import brsSwitch

# Title
print("brswitch v3.0s - made by skipster1337")
print("https://github.com/skipster1337/brswitch\n")

# Determine system type
print(f"You are running {brsProcess_System}.")

# Initiate configuration file
brsConfig_InitConf()

# Ask user to close Steam before proceeding
while True:
    choice = input(
        "\nbrswitch will quit Steam and Brick Rigs before proceeding. Continue? [Y/N]: "
    ).upper()
    if choice == "Y":
        # Attempt to kill Steam and Brick Rigs
        brsProcess_Kill("steam.exe")
        brsProcess_Kill("BrickRigs.exe")
        brsProcess_Kill("BrickRigs-Win64-Shipping.exe")

        # Display main menu
        while True:
            print("\n[S] Switch to stable")
            print("[L] Switch to legacy")
            print("[Q] Quit")

            # Convert inserted characters to uppercase for case insensitivity
            choice = input("Enter your choice: ").upper()
            if choice == "S":
                # Attempt to reset active branch before switching
                brsReset()
                # Run the branch switcher with the respective branch name
                brsSwitch("stable")
            elif choice == "L":
                brsReset()
                brsSwitch("legacy")
            elif choice == "Q":
                exit("Goodbye.")
            else:
                print("Invalid choice. Please select a valid option.")

    elif choice == "N":
        exit("Not quitting Steam, so brswitch cannot continue. Goodbye.")
    else:
        print("Invalid choice. Please select a valid option.")
