from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mt-4',
            'placeholder': 'example@email.com'})

        self.fields['username'].widget.attrs.update({
            'class': 'form-control mt-4',
            'placeholder': 'Username'})

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mt-4',
            'placeholder': 'Password'})

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mt-4',
            'placeholder': 'Password'})


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
