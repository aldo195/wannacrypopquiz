from django import forms

from .models import Drill


class PostForm(forms.ModelForm):

    class Meta:
        model = Drill
        fields = ('email',
                  'workstation_count_estimate',
                  'workstation_count_active',
                  'workstation_count_auth',
                  'has_report',)

    def __str__(self):
        return str(self.email)
