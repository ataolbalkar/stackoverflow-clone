from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

user = get_user_model()


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('username', 'location', 'title', 'about', 'website', 'twitter', 'github', 'full_name', 'profile_image')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-sm user-setting-text-input'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control form-control-sm user-setting-text-input',
                'placeholder': 'Enter your location'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-sm user-setting-text-input',
                'placeholder': 'No title has been set'
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control form-control-sm form-control-sm user-setting-text-area',
                'rows': 9,
            }),
            'website': forms.TextInput(attrs={
                'class': 'form-control form-control-sm user-setting-web-presence'
            }),
            'twitter': forms.TextInput(attrs={
                'class': 'form-control form-control-sm user-setting-web-presence'
            }),
            'github': forms.TextInput(attrs={
                'class': 'form-control form-control-sm user-setting-web-presence'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm user-setting-text-input',
                'placeholder': 'Shown to employers only if opt-in'
            }),
        }


class EmailSettingsForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('email', )

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control user-profile-email-input'
            })
        }


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["class"] = 'form-control'
        self.fields["password2"].widget.attrs["class"] = 'form-control'


class RegistrationForm(CreateUserForm):
    class Meta:
        model = user
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            })
        }


class SetUserUpForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('username', 'interested_tags', 'full_name', 'location', 'title')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
