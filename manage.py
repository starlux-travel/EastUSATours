#!/usr/bin/env python
import os
import sys
from pathlib import Path

def main():
    """Django's command-line utility for administrative tasks."""
    BASE_DIR = Path(__file__).resolve().parent
    sys.path.append(str(BASE_DIR))   # 確保 eastusatours package 能被找到

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eastusatours.settings.production")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
