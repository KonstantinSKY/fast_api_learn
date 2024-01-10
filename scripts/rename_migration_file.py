import os
import pathlib
import re
import sys
from datetime import datetime

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
MIGRATION_DIR = BASE_DIR / 'migrations/versions'


def rename_migration_file(file_path=''):
    if file_path == '':
        # Define the migrations directory (adjust as needed)
        file_path = find_latest_migration_file(MIGRATION_DIR)
        if file_path is None:
            print("No migration files found.")
            return
        print("Found  migration version for rename", file_path)
    old_name = os.path.basename(file_path)
    # print("Old name", old_name)
    if is_file_renamed(old_name):
        print(f"The file {old_name} has already been renamed.")
        return
    file_time = os.path.getmtime(file_path)
    formatted_time = datetime.fromtimestamp(file_time).strftime('%Y_%m_%d_%H:%M')
    print("File time", file_time, "=> Formatted time", formatted_time)

    #
    # Create the new filename
    new_file_name = f"{formatted_time}_{old_name}.py"
    # print("New file name", new_file_name)
    # # Rename the file
    os.rename(file_path, os.path.join(os.path.dirname(file_path), new_file_name))
    print(f"File renamed to: {new_file_name}")


def find_latest_migration_file(directory):
    # Get all migration files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.py')]
    # Sort files by modification date
    latest_file = max(files, key=os.path.getmtime, default=None)
    return latest_file


def is_file_renamed(filename):
    # Regular expression to match your filename format (YYYY_MM_DD_HH:MM_oldname.py)
    pattern = r'^\d{4}_\d{2}_\d{2}_\d{2}:\d{2}_.+\.py$'
    return re.match(pattern, filename) is not None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            rename_migration_file(arg)
    else:
        rename_migration_file()
