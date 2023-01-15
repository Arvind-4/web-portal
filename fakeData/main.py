import os
import sys
import random
import pathlib
from faker import Faker

PROJECT_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

PATHS = [
    str(PROJECT_BASE_DIR / "apps"),
    str(PROJECT_BASE_DIR / "apps" / "web"),
    str(PROJECT_BASE_DIR / "apps" / "web" / "backend"),
]


sys.path.extend(PATHS)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django
django.setup()


from django.db import transaction
from django.contrib.auth import get_user_model

from blog.models import Blog
from lorem import generateLoremIpsum

User = get_user_model()

fake = Faker()

NUM_USERS = 50
NUM_BLOGS = 10


@transaction.atomic
def handle():
    people = []
    for _ in range(NUM_USERS):
        person = {
            'email': fake.email(),
            'password': fake.password(),
        }
        User.objects.create(**person)

    for _ in range(NUM_BLOGS):
        blog = {
            'title': fake.sentence(),
            'description': fake.text(),
            'body': generateLoremIpsum(random.randint(1, 10)),
            'author': random.choice(people),
        }
        Blog.objects.create(**blog)

    return "Done"