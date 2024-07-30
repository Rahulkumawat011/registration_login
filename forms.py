from django import forms

from apps.core.models import User


# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=100,label='name')
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     phone_number = forms.IntegerField()
#     age = forms.IntegerField()

class StudentForm(forms.ModelForm):
    class Meta:
        model=User
        fields = "__all__"

