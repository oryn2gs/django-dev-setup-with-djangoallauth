from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from allauth.models import EmailAddress


class LoginForm(forms.Form):
    email = forms.EmailField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Email",
                    "id": "email",
                    "class": "form-control forms-input-fields"
                    }
                )
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "password",
                "id": "password",
                "class": "form-control forms-input-fields",
            },
        )
    )

    def clean(self):
        cleaned_data = self.super().clean()
        email = cleaned_data.get("email")

        if not EmailAddress.objects.filter(email=email).exist():
            raise ValidationError(
                message="User with that email doen't exists",
                code="invalid_email")

        return cleaned_data
