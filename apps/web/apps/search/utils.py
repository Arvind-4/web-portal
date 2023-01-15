from django.db.models import Q
from django.contrib.auth import get_user_model
from itertools import chain

from blog.models import Blog
from comments.models import Comment

User = get_user_model()

def performSearch(text):
    blogResults = Blog.objects.filter(
        Q(title__icontains=text) |
        Q(description__icontains=text) |
        Q(body__icontains=text)
    ).distinct()
    # commentResults = 
    userResults = User.objects.filter(
        Q(email__icontains=text)
    ).distinct()
    results = chain(blogResults, userResults)
    return results
