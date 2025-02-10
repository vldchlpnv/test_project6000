from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    first_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label='')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
                                    label='')

    class Meta:
        model = User  # Используем модель CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Имя пользователя или Email', 'autofocus': True}),
                               required=True)  # либо почта либо логин
    password = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Пароль'}),
                               required=True)
    remember_me = forms.BooleanField(required=False, label='Запомнить меня')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(self.request, username=username,
                                           password=password)  # атрибт формы который хранит в себе функцию authenticate()
            # после успешной аутентификации позволяет избежать повторной проверки учетных данных в других частях формы
            if self.user_cache is None:
                try:
                    user = User.objects.get(email=username)
                    self.user_cache = authenticate(self.request, username=user.username, password=password)
                except User.DoesNotExist:
                    pass

        if self.user_cache is None:
            raise self.get_invalid_login_error()
        else:
            self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data

        # def clean(self):
        #    username = self.cleaned_data.get("username")
        #    password = self.cleaned_data.get("password")

        #    if username is not None and password:
        #        self.user_cache = authenticate(
        #            self.request, username=username, password=password
        #        )
        #        if self.user_cache is None:
        #            raise self.get_invalid_login_error()
        #        else:
        #            self.confirm_login_allowed(self.user_cache)

        #      return self.cleaned_data
