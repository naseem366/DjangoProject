from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.db import models
from django.db.models import fields
from .models import *
 

class EditProfileForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['full_name','email']

    def clean(self):
      super(EditProfileForm, self).clean()

      # getting username and password from cleaned_data
      full_name = self.cleaned_data.get('full_name')
      
      # validating the username and password
      if len(full_name) < 4:
        self._errors['full_name'] = self.error_class(['A minimum of 4 characters is required'])
      return self.cleaned_data
      
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_number','profile_image'] #Note that we didn't mention user field here.
    


class CustomerRegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ('full_name','email',)

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')


class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField()
    newpassword = forms.CharField()
    conpassword = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'].strip = False
        self.fields['newpassword'].strip = False
        self.fields['conpassword'].strip = False

    def clean(self):
        oldpassword = self.cleaned_data.get('oldpassword')
        newpassword = self.cleaned_data.get('newpassword')
        conpassword = self.cleaned_data.get('conpassword')

        if not self.user.check_password(oldpassword):
            print('valid passs')
            raise forms.ValidationError('Please provide valid old password')

        if not len(newpassword) >= 8 or not len(conpassword) >=8:
            print('8')
            raise forms.ValidationError('Password must be atleast 8 characters long') 

        if newpassword != conpassword:
            print('same')
            raise forms.ValidationError('Both new password and confirm password must be same') 

        return self.cleaned_data 


