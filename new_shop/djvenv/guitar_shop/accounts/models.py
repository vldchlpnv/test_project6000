from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): # переопределяю User на кастомный класс добавил в настройках пункт AUTH_USER_MODEL = 'accounts.CustomUser'
# далее через from django.contrib.auth import get_user_model она ссылается на AUTH_USER_MODEL = 'accounts.CustomUser'
    email = models.EmailField(unique=True, verbose_name='Email address', blank=False)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL" # Заменим стандартный User



