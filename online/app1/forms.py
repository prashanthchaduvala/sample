from django import forms
from .models import Savemodel,Merchantmodel


# class Saveform(forms.ModelForm):
#     class Meta:
#         model= Savemodel
#         widgets = {
#             "password":forms.passwordInput(),
#         }


class SavemodelForm(forms.ModelForm):
    class Meta:
     model = Savemodel
     fields = "__all__"
