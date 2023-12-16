# brswitch v3.0s

Currently if you want to play multiple versions of your games on Steam, you typically have to either constantly switch branches and redownload, backup / restore, or even manage multiple Steam installs.

brswitch is a Python script which tries to automate the tedious task of switching between Brick Rigs' Steam branches. Currently it offers very basic functionality and only allows you to switch between the Stable (regular) and Legacy versions of the game, but more features will be added with time.

# How to install

You can set up brswitch in multiple ways, the easiest one is just running it directly with Python.

- [Install the latest version of Python for Windows](https://www.python.org/downloads/windows/). Click on "Latest Python 3 release", scroll down, download the "Windows Installer (64-bit), and then install it.
- Clone this repository or download it by clicking on the green "Code" button and going to "Download ZIP".
- Extract the `brswitch-main.zip` file with any archive manager. Make sure you're unpacking it and not running brswitch directly from the archive!

If this seems all too complicated for you, there will be a ready-to-run .exe file in the [Releases](https://github.com/skipster1337/brswitch/releases) section that you can use without having to install Python. The reason why it's recommended to run it directly with Python is because .py files are human-readable and therefore you can easily see what the script does.

# How to use

Once you've downloaded brswitch, you need to (optionally) configure it, and then set up your Brick Rigs folders and .appmanifest files to be compatible with it. This requires basic file management skills, and the script will guide you through the process in future versions.

### This is in-development (beta) software, make backups of your Brick Rigs folder and mods before proceeding!

Your saved vehicles will not be affected.

## First run

- Make sure you have file extensions _enabled_. In the File Explorer window click on the "View" menu and enable "File name extensions". This will help you differentiate between file types more easily.
- Once you've unpacked the archive, open `brswitch.py`, and then quit it. This will create the default configuration file (named `brswitch.conf`) in your user folder.

## Configuration

You must follow these steps to edit the configuration file if your Steam and Brick Rigs are not installed in the default C: drive location.

- Go to your user folder. The easiest way to do it is by opening the "Run" prompt with Win+R and typing in `%userprofile%`.
- In your user folder, find `brswitch.conf`. This is brswitch's configuration file which tells it the paths where Steam and Brick Rigs are installed.
- Open `brswitch.conf` with any text editor (such as Notepad).

In there, you will see two lines under the `[paths]` section:

```
[paths]
; Set this to the folder where Steam is installed
steam_location = C:\Program Files (x86)\Steam
; Set this to your steamapps\common folder
game_location = C:\Program Files (x86)\Steam\steamapps\common
```

You have to set `steam_location` to the folder where Steam is installed, and `game_location` to the `steamapps\common` folder where Brick Rigs is located, if you changed their locations from the defaults.

For example, my paths are set like so:

```
[paths]
steam_location = D:\Steam
game_location = D:\Steam\steamapps\common
```

_(This is just an example, your custom paths are probably different so don't copy mine)_

If you haven't changed Steam or Brick Rigs' install location, and they are installed in `C:\Program Files (x86)\`, this should not be required.

## Folder setup

With all that out of the way, all you need to do now is make sure your branches are correctly set up (future versions of brswitch will guide you through folder setup).

### Branch 1

- Quit Steam by right clicking on its tray icon and selecting "Exit Steam".
- Go to `steamapps\common` where Brick Rigs is installed.
- Rename the `Brick Rigs` folder to `br_<branch>`, where `<branch>` is the name of your currently installed Brick Rigs branch. If it's the regular branch, name it `br_stable`. If it's Legacy, name it `br_legacy`.
- Go up a folder to `steamapps`.
- Rename `appmanifest_552100.acf` to `br_<branch>.acf` (`br_stable.acf` for the regular branch and `br_legacy.acf` for Legacy).

### Branch 2

- Start Steam.
- Switch branches to the opposite of what you had before, and install Brick Rigs in the same place where your previous install was. If you had the regular branch, download Legacy, and if you had Legacy, download the regular branch.
- Quit Steam again.
- Rename the newly downloaded `Brick Rigs` folder to the respective `br_<branch>` that you just downloaded.
- Rename `appmanifest_552100.acf` to `br_<branch>.acf`.

If done correctly, your folder structure should look something like this:

`steamapps\common`:

```
📂 br_legacy
📂 br_stable
```

`steamapps`:

```
📄 br_legacy.acf
📄 br_stable.acf
```

### Done, brswitch should be ready to use now! Quit Steam, open brswitch and try switching branches.

If configured correctly, brswitch should succeed in switching the Stable and Legacy branches installed side-by-side.

# Removal

If you have decided to remove brswitch, you can easily do so by deleting the program from where you placed it, removing the `brswitch.conf` configuration file from your user folder, and finally, renaming your folders and `.appmanifest`s or backing up your Brick Rigs mods and reinstalling.
Sorry if brswitch brought you trouble.

# Manual building

If you feel dubious and want to compile the .exe yourself, all you need to do is download the repository and follow these steps:

- Install Python
- Install PyInstaller using pip: `pip install pyinstaller`
- Run `build.bat`. It will compile `brswitch.exe` based on the included `.spec` file, drop the binary in the `dist` folder, and create a log file named `build.log`.

# Linux (Proton) support

I am trying my best to make brswitch OS-agnostic and therefore compatible with any operating system that runs Python. However, I am not doing any active testing on Linux, so if you're interested in this project and run Brick Rigs under Proton, I encourage you to try this script and let me know if it works.

# Using brswitch for another project

If you feel inspired by this project and want to use it for yourself, you can! I try my best to comment the Python code as cleanly as possible, so it should be trivial to adapt it for any other Steam game or make modifications to the script. Just make sure to credit me if you do it.

# To do

## for v3.0s

- ~~Write a simple readme showing how to use the program~~
- ~~Clean up the code to use less redundant variables where possible~~
- ~~Write better comments~~
- ~~Make sure the script is cross-platform and does not rely on any OS features~~

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
