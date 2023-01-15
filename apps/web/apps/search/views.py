from django.shortcuts import render
from django.views.generic import View

from .models import Search
from .forms import SearchForm
from .utils import performSearch

# Create your views here.

class SearchView(View):
    context = {}
    templateName = 'search/view.html'
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data.get('q') 
            if request.user.is_authenticated: 
                user = request.user
            else:
                user = None
            obj, created = Search.objects.get_or_create(search=q, user=user)
            self.context['results'] = performSearch(q)
        self.context['form'] = form
        return render(request, self.templateName, self.context)