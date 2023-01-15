from django.shortcuts import render
from django.views.generic import View

# Create your views here.

image1 = "https://images.unsplash.com/photo-1499750310107-5fef28a66643?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"

image2 = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
class HomePageView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        self.context['image1'] = image1
        self.context['image2'] = image2
        return render(request, 'pages/home.html', self.context)

class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/about.html', {})

class ContactPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/contact.html', {})