from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.views.generic import View

from comments.models import Comment
from comments.forms import CommentForm
from .models import Blog
from .forms import BlogCreateForm

# Create your views here.

class BlogHomeView(View):
    def get(self, request):
        blogs = tuple(Blog.objects.all())
        top5Blogs = blogs[:5]
        restBlogs = blogs[5:]
        context = {
            'top5Blogs': top5Blogs,
            'restBlogs': restBlogs,
        }
        return render(request, 'blog/home.html', context)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = BlogCreateForm()
        return render(request, 'blog/create.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            obj = Blog.objects.create(title=title, content=content)
            return render(request, 'blog/create.html', {'form': form})
        else:
            return render(request, 'blog/create.html', {'form': form})

class BlogDetailView(View):
    context = {}
    templateName = 'blog/detail.html'
    def get(self, request, id, *args, **kwargs):
        form = CommentForm()
        blog = get_object_or_404(Blog, id=id)
        comments = blog.comments.filter(active=True)
        self.context['form'] = form
        self.context['blog'] = blog
        self.context['comments'] = comments
        return render(request, self.templateName, self.context)

    def post(self, request, id, *args, **kwargs):
        form = CommentForm(request.POST)
        blog = get_object_or_404(Blog, id=id)
        comments = blog.comments.filter(active=True)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog = blog
            new_comment.save()
            return redirect(blog.get_absolute_url()+'#'+str(new_comment.id))
        self.context['form'] = form
        self.context['blog'] = blog
        self.context['comments'] = comments
        return render(request, self.templateName,self.context)


 

class BlogUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        blog = get_object_or_404(Blog, id=id)
        form = BlogCreateForm(initial={'title': blog.title, 'content': blog.content})
        return render(request, 'blog/update.html', {'form': form, 'blog': blog})

    def post(self, request, *args, **kwargs):
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            obj = Blog.objects.create(title=title, content=content)
            return render(request, 'blog/update.html', {'form': form})
        return render(request, 'blog/update.html', {'form': form})


class BlogDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        blog = Blog.objects.get(id__iexact=id)
        blog.delete()
        return redirect('index')