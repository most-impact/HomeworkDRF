import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название курса",
                        max_length=240,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью",
                        null=True,
                        upload_to="course/preview",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание курса",
                        null=True,
                        verbose_name="описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название урока",
                        max_length=240,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "preview_lesson",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью урока",
                        null=True,
                        upload_to="course/preview_lesson",
                        verbose_name="Превью урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание урока",
                        null=True,
                        verbose_name="описание урока",
                    ),
                ),
                (
                    "reference",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="course.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
                "ordering": ["title"],
            },
        ),
    ]