from platform import system
import psutil
import time
import subprocess
from brsConfig import brsConfig_ReadSteamLocation

# Determine system type
brsProcess_System = system()

def brsProcess_Kill(process_name):
    process_found = False

    for process in psutil.process_iter(["pid", "name"]):
        if process.info["name"] == process_name: # type: ignore
            pid = process.info["pid"] # type: ignore
            try:
                # Attempt to terminate the process
                process = psutil.Process(pid)
                if psutil.pid_exists(pid):
                    process.terminate()

                # Wait for a bit before trying to kill again
                time.sleep(0.25)

                # If the process is still alive after termination, force kill it
                if psutil.pid_exists(pid):
                    process.kill()

                print(f"Process {process_name} with PID {pid} terminated successfully.")
                process_found = True
            except Exception as e:
                print(f"Error terminating process {process_name} with PID {pid}: {e}")
    # Raise an exception if the process was not found
    if not process_found:
        print(f"Process {process_name} not found.")

def brsProcess_StartSteam():
    brsConfig_SteamLocation, brsConfig_SteamExe = brsConfig_ReadSteamLocation()
    subprocess.Popen(brsConfig_SteamExe)
    print("Started Steam.")