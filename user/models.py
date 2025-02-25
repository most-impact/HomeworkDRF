from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    number = models.CharField(
        max_length=35,
        help_text="Укажите ваш номер телефона",
        verbose_name="Номер телефона",
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=150, help_text="Укажите ваш город", verbose_name="Город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите фото",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
