from django import forms
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()


class EmployeesForm(forms.ModelForm):
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    profession = forms.CharField(required=True)
    mobile = forms.CharField(required=True)
    website = forms.CharField(required=True)
    activity = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'profession',
                  'email', 'mobile', 'website', 'social_link', 'activity')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('user', 'company_name')
