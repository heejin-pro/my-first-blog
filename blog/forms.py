from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class SampleForm(forms.Form):

    sample_text = forms.CharField(initial="Sample Text Field~")
