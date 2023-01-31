:: brswitch - Brick Rigs Automatic Branch Switcher
:: v2.2.1
:: skipster1337 - 2023
:: https://github.com/skipster1337/brswitch

:: Set this to your Steam path (where the Steam program is located), without "quotes" and without a \slash\ at the end.
:: Default:
:: set steam_path=C:\Program Files (x86)\Steam
:: Examples of custom paths:
:: set steam_path=D:\Steam
:: set steam_path=D:\Programs\Steam
set steam_path=C:\Program Files (x86)\Steam

:: Set this to your steamapps\common\ folder (where the Brick Rigs folder is located), without "quotes" and without a \slash\ at the end
:: Default:
:: set br_path=C:\Program Files (x86)\Steam\steamapps\common
:: Examples of custom paths:
:: set br_path=D:\Steam\steamapps\common
:: set br_path=E:\Games\SteamLibrary\steamapps\common
set br_path=C:\Program Files (x86)\Steam\steamapps\common

:: Do not edit anything below or the script might break.


:: Don't display commands entered by script
@echo off

:: Console window title
set version=v2.2.1
title brswitch %version% - skipster1337 - 2023

:: Change location to path where BR is located for file operations
cd %br_path%


:: Title and warning
echo.
echo brswitch - Brick Rigs Automatic Branch Switcher %version%
echo https://github.com/skipster1337/brswitch
echo Message me on Discord: @skip#9831
echo.
echo NOTE:
echo You need to set your Steam and Brick Rigs paths correctly for brswitch to work.
echo You can do that by opening the file in a text editor and changing the lines at the beginning.
echo.
echo Also, brswitch may fail if your game paths are messed up, such as incorrect folder naming or broken .appmanifest files.
echo If it fails, try backing up your game files (or mods) and reinstalling.
echo.
choice /m "brswitch will close Steam. Continue?"
if errorlevel 0 (
  set jumplabel=errorhandler
)
if errorlevel 1 (
  set jumplabel=menu
)
if errorlevel 2 (
  exit /b
)
if errorlevel 255 (
  set jumplabel=errorhandler
)
goto %jumplabel%
pause
exit /b


:: Menu used for choosing branch switcher actions
:menu
taskkill /t /f /im steam.exe 2>NUL
taskkill /t /f /im BrickRigs.exe 2>NUL
taskkill /t /f /im BrickRigs-Win64-Shipping.exe 2>NUL
echo.
echo Select what you want to do:
echo [1] Set up the Brick Rigs folder structure
echo [2] Set up the experimental version
echo [3] Set up a historical version
echo [S] Switch to stable
echo [L] Switch to legacy
echo [E] Switch to experimental
echo [H] Switch to historical
echo [Q] Quit
choice /C 123SLEHQ
if errorlevel 0 (
  set jumplabel=errorhandler
)
if errorlevel 1 (
  set jumplabel=create_structure
)
if errorlevel 2 (
  set jumplabel=create_experimental
)
if errorlevel 3 (
  set jumplabel=create_historical
)
if errorlevel 4 (
  set branch=stable
  set jumplabel=switcher
)
if errorlevel 5 (
  set branch=legacy
  set jumplabel=switcher
)
if errorlevel 6 (
  set branch=experimental
  set jumplabel=switcher
)
if errorlevel 7 (
  set branch=historical
  set jumplabel=switcher
)
if errorlevel 8 (
  exit /b
)
if errorlevel 255 (
  set jumplabel errorhandler
)
goto %jumplabel%
pause
exit /b


:: Creates the folders and appmanifests for branch switching
:create_structure
if exist ..\br_*.acf (
  echo.
  echo You have set up your folder structure already. If you want to remake it, back up your current Brick Rigs files somewhere else and reinstall.
  pause
  goto menu
)
echo.
echo Is your Brick Rigs branch currently set to stable or legacy?
echo Press S or L accordingly.
choice /C sl
if errorlevel 0 (
  set jumplabel=errorhandler
)
if errorlevel 1 (
  set old_branch=stable
  set new_branch=legacy
  set jumplabel=start_create_structure
)
if errorlevel 2 (
  set old_branch=legacy
  set new_branch=stable
  set jumplabel=start_create_structure
)
goto %jumplabel%
pause
exit /b

:start_create_structure
echo.
echo Setting up the %new_branch% branch.
echo renaming the "Brick Rigs" folder to "br_%old_branch%".
ren "Brick Rigs" br_%old_branch%
echo renaming "appmanifest_552100.acf" to "br_%old_branch%.acf".
ren ..\appmanifest_552100.acf br_%old_branch%.acf
echo.
echo brswitch will open Steam to continue the process.
pause
start "Steam" "%steam_path%\steam.exe"
echo Now you have to open Steam and download the %new_branch% branch. Only continue once the download is finished.
pause
echo brswitch will close Steam again in order to continue the process.
pause
echo.
taskkill /t /f /im steam.exe 2>NUL
taskkill /t /f /im BrickRigs.exe 2>NUL
taskkill /t /f /im BrickRigs-Win64-Shipping.exe 2>NUL
echo renaming the "Brick Rigs" folder to "br_%new_branch%".
ren "Brick Rigs" br_%new_branch%
echo renaming "appmanifest_552100.acf" to "br_%new_branch%.acf".
ren ..\appmanifest_552100.acf br_%new_branch%.acf
echo.
choice /m "Done. Now you have both branches ready. Do you also want to set up experimental?"
if errorlevel 0 (
  set jumplabel=errorhandler
)
if errorlevel 1 (
  set jumplabel=create_experimental
)
if errorlevel 2 (
  set jumplabel=menu
)
if errorlevel 255 (
  set jumplabel=errorhandler
)
goto %jumplabel%
pause
exit /b


:: Creates the experimental branch
:: Reset branches before creating experimental to avoid broken files
:create_experimental
set reset_reason=start_create_experimental
goto reset

:start_create_experimental
:: Don't set up experimental if folder structure is not set up yet
if not exist ..\br_*.acf (
  echo.
  echo You haven't set up the folder structure yet! To set up experimental, you need legacy or stable first.
  pause
  goto menu
)
:: Don't set up experimental if already installed
if exist "br_experimental" (
  echo.
  echo You already have experimental installed. No need to set it up again.
  pause
  goto menu
)
echo.
echo brswitch will open Steam. Continue?
pause
start "Steam" "%steam_path%\steam.exe"
echo Open Steam and download the experimental branch. Only continue once the download is finished.
pause
echo brswitch will close Steam again in order to continue the process.
pause
echo.
taskkill /t /f /im steam.exe 2>NUL
taskkill /t /f /im BrickRigs.exe 2>NUL
taskkill /t /f /im BrickRigs-Win64-Shipping.exe 2>NUL
echo renaming "Brick Rigs" folder to "br_experimental".
ren "Brick Rigs" br_experimental
echo renaming "appmanifest_552100.acf" to "br_experimental.acf".
ren ..\appmanifest_552100.acf br_experimental.acf
echo.
echo Done, experimental is set up. Continue to switch to the desired branch.
pause
goto menu


:: Creates the historical branch (WIP)
:create_historical
echo.
echo WIP.
echo.
pause
goto menu


:: Reset already selected branch before switching, otherwise the branch switcher won't know what to do
:: This is done using some simple guessing with if statements
:: Order is stable, legacy, experimental, historical

:: Cursed code, not touching this
:reset
if exist "Brick Rigs" (
  if exist ..\br_*.acf (
    if not exist "br_stable" (
      set branch_to_reset=stable
    ) else (
      if not exist "br_legacy" (
        set branch_to_reset=legacy
      ) else (
        if not exist "br_experimental" (
          set branch_to_reset=experimental
        ) else (
          if not exist "br_historical" (
            set branch_to_reset=historical
          )
        )
      )
    )
    goto reset_branch
  ) else (
    echo.
    echo You haven't set up the folder structure yet! Not switching to avoid broken files.
    pause
    goto menu
  )
) else (
  goto %reset_reason%
)

:: Renames the folders to their codenames in order to reset the selected branch
:reset_branch
echo.
echo Current branch is %branch_to_reset%.
echo Resetting selected branch before proceeding.
echo.
echo Renaming the "Brick Rigs" folder to "br_%branch_to_reset%".
ren "Brick Rigs" br_%branch_to_reset%
echo Renaming "appmanifest_552100.acf" to "br_%branch_to_reset%.acf".
ren ..\appmanifest_552100.acf br_%branch_to_reset%.acf
goto %reset_reason%


:: The branch switcher code itself
:switcher
:: Reset branches before switching to avoid broken files
set reset_reason=switch_branch
goto reset

:switch_branch
:: Don't switch if selected branch does not exist
if not exist "br_%branch%" (
  echo.
  echo You don't have %branch% installed! Can't switch to missing branch.
  pause
  goto menu
)
echo.
echo Switching to %branch%.
echo Renaming "br_%branch%" folder to "Brick Rigs".
ren br_%branch% "Brick Rigs"
echo Renaming "br_%branch%.acf" to "appmanifest_552100.acf".
ren ..\br_%branch%.acf appmanifest_552100.acf
echo.
choice /m "Done. Do you want to open Steam?"
if errorlevel 0 (
  set jumplabel=errorhandler
)
if errorlevel 1 (
  set jumplabel=startsteam
)
if errorlevel 2 (
  exit /b
)
if errorlevel 255 (
  set jumplabel=errorhandler
)
goto %jumplabel%
pause
exit /b


:: Misc functions
:startsteam
start "Steam" "%steam_path%\steam.exe"
goto terminate

:errorhandler
echo An error has occurred. Quitting...
goto terminate

:terminate
pause
exit /b