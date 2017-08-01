from django import forms

from .models import Drill


class PostForm(forms.ModelForm):

    class Meta:
        model = Drill
        fields = ('title', 'email',)