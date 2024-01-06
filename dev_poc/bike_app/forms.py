''''
from django import forms
from django.core import validators
from bike_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

'''

''''
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField()
    verify_password = forms.CharField(label='Enter your password again:')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        password = all_clean_data['password']
        mpassword = all_clean_data['verify_password']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
        if password != mpassword:
            raise forms.ValidationError("MAKE SURE password MATCH!")
    '''

from django import forms
from django.contrib.auth.models import User
from bike_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')