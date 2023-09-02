from brs_configurator import brs_initconf
from brs_resetter import brs_reset

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

    choice = input("Enter your choice: ").upper()

    if choice == "S":
        print("\nSwitching to stable.")
        # Attempt to reset active branch before switching
        brs_reset()
    elif choice == "L":
        print("\nSwitching to legacy.")
        brs_reset()
    elif choice == "Q":
        print("Goodbye.")
        break  # Exit the menu loop

    else:
        print("Invalid choice. Please select a valid option.")