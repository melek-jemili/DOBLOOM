from django import forms

from .models import *



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'to_be_done_before']  # inclure 'completed'
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Add a description for your task...'
            }),
            'completed': forms.CheckboxInput(attrs={
                'style': 'width: 20px; height: 20px;'
            }),
            'to_be_done_before': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }),
            }
        
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



