from django import forms

from .models import Drill


class DrillForm(forms.ModelForm):

    class Meta:
        model = Drill
        fields = '__all__'

    def __str__(self):
        return str(self.drill_id)
