import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import reviews.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=256,
                        unique=True,
                        verbose_name="название категории",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        unique=True, verbose_name="slug категории"
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Комментарий")),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата публикации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарии",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=256,
                        unique=True,
                        verbose_name="название жанра",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(unique=True, verbose_name="slug жанра"),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="GenresTitles",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Отзыв")),
                (
                    "score",
                    models.IntegerField(
                        help_text="Поставьте оценку от 1 до 10",
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="Оценка",
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата публикации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзывы",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.CreateModel(
            name="Title",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="название"),
                ),
                (
                    "year",
                    models.PositiveIntegerField(
                        validators=[reviews.validators.custom_year_validator],
                        verbose_name="год выпуска",
                    ),
                ),
                (
                    "rating",
                    models.IntegerField(
                        default=None, null=True, verbose_name="рейтинг"
                    ),
                ),
                ("description", models.TextField(verbose_name="описание")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="titles",
                        to="reviews.Category",
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        default=None,
                        related_name="titles",
                        through="reviews.GenresTitles",
                        to="reviews.Genre",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
