from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=''  # Retire le texte d’aide
    )

    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=''  # ➜ Retire ce message que tu vois
    )
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': '',
            'password1': '',
            'password2': '',
        }

       

class CustomAuthenticationForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CreationPersonnel(CustomUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['role'].choices = [
            choice for choice in CustomUser.ROLE_CHOICES
            if choice[0] in ['serveur', 'cuisinier'] 
        ]

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
       


