from brs_configurator import brs_initconf
from brs_resetter import brs_reset
from brs_switcher import brs_switcher

# Title
print("brswitch v3.0rw - made by skipster1337")
print("https://github.com/skipster1337/brswitch\n")

# Initialize brswitch configuration
brs_initconf()

# Warn user to close Steam before proceeding
print("\nPlease make sure you exit Steam before proceeding.")

# Menu choices
while True:
    print("\n[S] Switch to stable")
    print("[L] Switch to legacy")
    print("[Q] Quit")

    # Convert inserted characters to uppercase for case insensitivity
    choice = input("Enter your choice: ").upper()

    if choice == "S":
        # Attempt to reset active branch before switching
        brs_reset()
        # Run the branch switcher with the respective branch name
        brs_switcher("stable")
    elif choice == "L":
        brs_reset()
        brs_switcher("legacy")
    elif choice == "Q":
        print("Goodbye.")
        break  # Exit the menu loop

    else:
        print("Invalid choice. Please select a valid option.")
