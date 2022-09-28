#!/usr/bin/env python
import os
import sys

# DJANGO_SETTINGS_MODULE defines the correct settings for the environment where your app is running
# i-e development or production

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btre.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
