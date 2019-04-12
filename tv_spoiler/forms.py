from django.forms import ModelForm, forms

from .models import Victim


class VictimForm(ModelForm):
    class Meta:
        model = Victim


class SpoilForm(forms.Form):
    pass
