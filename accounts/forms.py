from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User, UserProfile


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    # username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].icon = '<span class="input-field-icon"><i class="fas fa-envelope"></i></span>'
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter Last Name'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Again password'})
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2")

        # widgets = {
        #     'password1': forms.TextInput(attrs={'placeholder': 'Password'}),
        #     'password2': forms.TextInput(attrs={'placeholder': 'Repeat your password'}),
        # }

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Enter valid email')
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({'placeholder': 'Title'})
        self.fields["phone"].widget.attrs.update({'placeholder': 'Phone'})
        self.fields["country"].widget.attrs.update({'placeholder': 'Country'})
        self.fields["city"].widget.attrs.update({'placeholder': 'City'})
        self.fields["Institute"].widget.attrs.update({'placeholder': 'Institute'})
        self.fields["occupation"].widget.attrs.update({'placeholder': 'Occupation'})
        self.fields["profile_pic"].widget.attrs.update({'placeholder': 'Occupation'})
        self.fields["facebook"].widget.attrs.update({'placeholder': 'Facebook'})
        self.fields["twitter"].widget.attrs.update({'placeholder': 'Twitter'})
        self.fields["linkedin"].widget.attrs.update({'placeholder': 'LinkedIn'})

    class Meta:
        model = UserProfile
        fields = ["title", "phone", "country", "city", "Institute", "occupation", "address", "profile_pic", "facebook",
                  "twitter",
                  "linkedin"]
