from django import forms
from fourth_app.models import user

class NewUser(forms.ModelForm):
    class Meta():
        model=user
        fields='__all__'