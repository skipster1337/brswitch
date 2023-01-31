# brswitch
brswitch is a simple script that lets you switch branches for the Steam game Brick Rigs. Currently it allows setting up the three branches of the game side by side (stable, legacy and experimental) and future releases will guide you in installing an older version of the game as a switchable 'historical' branch.  

brswitch is written in the Windows Batch scripting language which makes it easily hackable and modifiable with the right knowledge, so if you want to use this for another project, you can.  

brswitch works by renaming the game folder and .appmanifest file for the each branch to a codename (like `br_stable`) and keeping them for later. When switching, said codenamed folders are simply renamed to the filenames expected by Steam. This is more efficient than messing with Windows' "symbolic links" because they are somewhat unstable (in my tests, the .appmanifest file's symlink would just merge with every other version, making a huge mess that Steam didn't know what to do with). Renaming is much simpler and is done with some guessing using logic statements in Batch.

# Cool, cool. How do I use this?
- Follow [this link](https://raw.githubusercontent.com/skipster1337/brswitch/main/brswitch.bat) and save the batch file by pressing CTRL+S.
- It should download a .bat file which you will have to put in your `Steam\steamapps\common` folder (or wherever the `Brick Rigs` folder is located for you).
- Open `brswitch.bat` and follow the instructions.

**Note:** an easy way to find your `steamapps\common` directory is to right click on Brick Rigs in your Steam library, choose to browse the local files and go up a level to `common`. That's where you have to save the script.