from django.urls import path, re_path, include
from .views import *
from django.contrib.auth import views as auth_views

#app_name = 'accounts' # почему то не отрабатывает с app_name и namespace

urlpatterns = [path('sign_up/', SignUpView.as_view(), name='sign_up'),
               path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html') ,name='login'),
               path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout')
               ]