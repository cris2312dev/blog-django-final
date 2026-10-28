from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username']:
            self.fields[fieldname].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control' if 'password' in self.fields else None
        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs['class'] = 'form-control'
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs['class'] = 'form-control'

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Cuéntanos un poco sobre ti...'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://tusitio.com'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
