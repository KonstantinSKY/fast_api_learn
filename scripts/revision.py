import subprocess
import sys
import os
import pathlib
from rename_migration_file import rename_migration_file


def run_alembic_revision(message=''):
    alembic_dir = pathlib.Path(__file__).resolve().parent.parent
    os.chdir(alembic_dir)
    if not os.path.exists('alembic.ini'):
        print("Alembic configuration file not found.", os.getcwd(), alembic_dir)
        return

    try:
        # Constructing the Alembic command
        command = ["alembic", "revision", "--autogenerate", "-m", message]

        # Running the command
        subprocess.run(command, check=True)
        print("Alembic migration generated successfully by revision.py.")
        rename_migration_file()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the migration: {e}", file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
        run_alembic_revision(message)
    else:
        run_alembic_revision()
