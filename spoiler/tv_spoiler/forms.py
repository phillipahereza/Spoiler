from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms

from .models import Victim


class VictimForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = ['name', 'telephone_number']
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control input-lg',
            }),
            'telephone_number': forms.fields.TextInput(attrs={
                'placeholder': '+256782000000',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(VictimForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('telephone_number', css_class='form-control'),

            Submit('submit', 'Submit', css_class='btn btn-primary'),

        )


class SpoilForm(forms.Form):
    spoil_text = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!')

    def __init__(self, *args, **kwargs):
        super(SpoilForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('spoil_text', css_class='form-control'),

            Submit('submit', 'Submit', css_class='btn btn-primary'),)


class OptOutForm(forms.Form):
    telephone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+256782000000'}))

    def __init__(self, *args, **kwargs):
        super(OptOutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('telephone_number', css_class='form-control'),

            Submit('submit', 'Opt Out', css_class='btn btn-primary'),)


