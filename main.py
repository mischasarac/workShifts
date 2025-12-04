from workRequest import getWorkHTML
from htmlParser import getShifts
from calendarInteractions import addShiftsToCalendar
from validateNewShifts import validateNewShifts
import os

ENV_FILE = ".env"
REQUIRED_KEYS = ["USERNAME", "PASSWORD"]


def read_env_file():
    """Read key-value pairs from .env into a dict."""
    if not os.path.exists(ENV_FILE):
        return {}

    env = {}
    with open(ENV_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                env[key] = value
    return env


def write_env_file(values):
    """Write the provided key-value pairs into .env."""
    with open(ENV_FILE, "w") as f:
        for k, v in values.items():
            f.write(f"{k}={v}\n")


def load_credentials():
    """
    Load USERNAME and PASSWORD from .env.
    If missing or file doesn't exist, prompt user and write file.
    Returns: (username, password)
    """
    env = read_env_file()

    missing = [k for k in REQUIRED_KEYS if k not in env]

    if missing:
        print("Missing credentials in .env — please enter them now.")
        for key in missing:
            env[key] = input(f"Enter your {key.lower()}: ")

        write_env_file(env)

    return env["USERNAME"], env["PASSWORD"]


if __name__ == "__main__":
    # Load credentials cleanly
    username, password = load_credentials()

    # Now call your workflow
    pageHTML = getWorkHTML(username, password)
    upComingShifts = getShifts(pageHTML)
    newShifts = validateNewShifts(upComingShifts)

    if not newShifts:
        print("No new shifts to append")
    else:
        print("Adding shifts...")
        addShiftsToCalendar(upComingShifts)
