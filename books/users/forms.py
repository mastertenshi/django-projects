from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm
)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


def add_attr(fields):
    for field in fields:
        fields[field].widget.attrs.update({
            'class': 'form-control',
            'placeholder': f'{field.capitalize()}'
        })
