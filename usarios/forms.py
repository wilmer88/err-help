from dataclasses import field
from django import forms
from .models import ErrModel


class ErrForm(forms.ModelForm):
    class Meta:
        model=ErrModel
        fields = ["lang_name","err_title","fixer_code","os_tech"]
 