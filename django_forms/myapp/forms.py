from django import forms
from .parse import parse



from .load_json import denest
from django.forms import ModelForm, Form
from django_jsonforms.forms import JSONSchemaField


#class UseCaseForm(forms.Form):
 #   use_type = forms.ChoiceField(choices=[('simple', 'Simple box model'),('csv', 'Box model with csv data')])


class CustomForm(forms.Form):
    use_type = forms.ChoiceField(choices=[('simple', 'Simple box model'), ('csv', 'Box model with csv data')])
    def __init__(self, *args, **kwargs):
        dynamic_fields = denest()
        super(CustomForm, self).__init__(*args, **kwargs)
        for key in dynamic_fields:
            self.fields[key] = forms.CharField(initial=dynamic_fields[key])
