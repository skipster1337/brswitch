# brswitch v3.0 rewrite

I lost a big portion of the previous .py file somehow so I just nuked everything and started over. Now I actually split my code into separate files and define chunks of code as functions so it's much tidier and sane.  
The first working release of the rewrite version will only offer basic branch switching functionality, but more features will be added in the future.  
This readme file is also a placeholder. I will rewrite it with the first release.

# how to install

You can set up brswitch in multiple ways, the easiest one is just running it directly with Python.
- [Install the latest version of Python for Windows](https://www.python.org/downloads/windows/)
- Clone this repository or download it by clicking on the green "Code" button and going to "Download ZIP"
- Unpack the `.zip` file with 7-Zip or WinRAR. Make sure you're unpacking it and not running it directly from the archive!
- Once you've unpacked the archive, open `brswitch.py` (or simply `brswitch` if you have file extensions disabled, *not* `brswitch.conf` or `brswitch.spec`)

If this seems all too complicated for you, there will be a ready-to-run .exe file in the Releases section that you can download. The reason I recommend that you run it directly is because Python files are human-readable and therefore you can see what the script does.

# manual building
If you want to compile the .exe yourself, all you need to do is download the repository and follow these steps:
- Install Python
- Install PyInstaller using pip: `pip install pyinstaller`
- Run `build.bat`. It will compile `brswitch.exe` based on the included `.spec` file, drop the binary in the `dist` folder, and create a log file named `build.log`.

# linux (proton) support
I am trying my best to make brswitch OS-agnostic and therefore compatible with any operating system that runs Python. However, I am not doing any active testing on Linux, so if you're interested in this project and run Brick Rigs under Proton, I encourage you to try this script and let me know if it works.


# todo

## for v3.0s

- Write a simple readme showing how to use the program
- Clean up the code to use less redundant variables where possible
- Write better comments
- Make sure the script is cross-platform and does not rely on any OS features
  
Essentially first working version, don't expect much beyond basic functionality

## for v3.1

- Write a better, more in-depth readme
- Cover more edge cases within the script and use the readme to explain the errors
- Add support for branch creation within the script
- Add support for automatically closing and starting Steam for convenience
- Add support for switching to experimental branch
  
Feature parity with first version written in batch

## for v3.2

- Add support for "historical" branch (older versions of the game stored as Steam depots)
- Add support for dev branch switching

## for v3.3

- Add support for historical branch creation within the script (guides you through opening the console and downloading depots)
