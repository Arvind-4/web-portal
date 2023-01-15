from django import forms
from ckeditor.widgets import CKEditorWidget


from .models import Blog


classNameInput = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

classNameTextArea = "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

class BlogCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(BlogCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'placeholder': 'Enter title', 
            'class': classNameInput
        }
        self.fields['content'].widget.attrs = {
            'placeholder': 'Enter content', 
            'class': classNameTextArea,
            'rows': 8
        }
        

