from django import forms
from .models import Comment


className = "px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 dark:text-white dark:placeholder-gray-400 dark:bg-gray-800"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs = {
            'placeholder': 'Write a comment...', 
            'class': className,
            'rows': 4
        }

    
    
    # overriding default form setting and adding bootstrap class
    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs = {'placeholder': 'Enter name','class':'form-control'}
    #     self.fields['email'].widget.attrs = {'placeholder': 'Enter email', 'class':'form-control'}
    #     self.fields['body'].widget.attrs = {'placeholder': 'Comment here...', 'class':'form-control', 'rows':'5'}