from django.contrib.auth.models import AbstractUser
from django.db import models
from course.models import Course, Lesson

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


class Payments(models.Model):
    PAYMENT_STATUS = [
        ("cash", "наличные"),
        ("transfer", "перевод на счет"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name="Пользователь")
    payment_date = models.DateField(null=True, blank=True, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course', verbose_name="Оплаченный курс", null=True, blank=True)
    separately_paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson', verbose_name="Оплаченный урок", null=True, blank=True)
    payment_amount = models.IntegerField(default=0, verbose_name='Сумма оплаты', blank=True, null=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='cash', verbose_name='Способ оплаты', null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.paid_course}'

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
