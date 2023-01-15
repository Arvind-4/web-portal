import os
import sys
import pathlib

PROJECT_BASE_DIR = pathlib.Path(__file__).resolve().parent

PATHS = [
    str(PROJECT_BASE_DIR / "apps"),
    str(PROJECT_BASE_DIR / "apps" / "web"),
    str(PROJECT_BASE_DIR / "apps" / "web" / "backend"),
]

sys.path.extend(PATHS)

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import django
django.setup()

from apps.web.backend.asgi import application
app = application