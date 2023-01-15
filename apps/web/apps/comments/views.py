from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

from blog.models import Blog
from .models import Comment
from .forms import CommentForm

# Create your views here.

class CommentReply(View):
    def post(self, request:HttpResponse, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            blogId = request.POST.get('blogId')  # from hidden input
            parentId = request.POST.get('parent')  # from hidden input
            blogUrl = request.POST.get('blogUrl')  # from hidden input
            print("blogId: ", blogId)
            print("parentId: ", parentId)
            print("blogUrl: ", blogUrl)
            reply = form.save(commit=False)
            reply.blog = Blog(id=blogId)
            reply.parent = Comment(id=parentId)
            reply.save()
            return redirect(f'{blogUrl}#{reply.id}')
        return redirect(request.url)