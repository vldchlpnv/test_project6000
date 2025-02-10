from django.shortcuts import render, redirect
from django.views import generic
# from django.contrib.auth.forms import UserCreationForm # данный класс содержит форму для создание пользователя через переменную form_class
from django.urls import reverse_lazy  # функция для перенаправения при успешной регистрации - напрмер
from .forms import *
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpView(
    generic.CreateView):  # базовый класс CreateView лежит в файле generic->edit.py "представление для регистрации"
    form_class = SignUpForm  # класс формы для регистрации на основе UserCreationForm если использовать чистый UserCreationForm там будет только логин и пароль с подтверждением
    success_url = reverse_lazy(
        "login")  # login это имя маршрута куда перенаправляется пользователь после успешной регистрации берется из urls.py
    template_name = "registration/signup.html"  # шаблон который будет рендерится
    initial = None  # {key:value} для автозаполнения полей формы тем что указано в словаре

    def dispatch(self, request, *args, **kwargs):    # перенаправит на домашнюю страницу, если пользователь попытается получить доступ к странице регистрации после авторизации
        if request.user.is_authenticated:
            return redirect(to='/')
        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data[
                'username']  # регистрация произведена успешно {user_name}', extra_tags='register')
            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def valid_form(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0) # установка времени жизни сесиии будет закрыта после выхода из браузера
            self.request.session.modified = True # обновляет состояние сессии
        return super(CustomLoginView, self).form_valid(form) # вызывается родительский метод form_valid,
                                                             # который завершает процесс входа пользователя в систему


