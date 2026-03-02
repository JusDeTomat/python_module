from sys import prefix, base_prefix, executable, path
from os import environ, path as pt


def main():
    if (in_venv()):
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {executable}")
        print(f"Virtual Environment: {pt.basename(environ['VIRTUAL_ENV'])}")
        print("""
SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.
            """)
        print("Package installation path:")
        print(next(p for p in path if 'site-packages' in p))
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {executable}")
        print("Virtual Environment: None detected\n\n"
              "WARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n\n"
              "To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate  # On Unix\n"
              "matrix_env\n"
              "Scripts\n"
              "activate      # On windows\n\n"
              "Then run this program again")


def in_venv():
    return prefix != base_prefix


if (__name__ == "__main__"):
    main()
