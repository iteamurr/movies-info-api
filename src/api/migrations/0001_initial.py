# Generated by Django 4.2.5 on 2023-09-08 20:24

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "movie_id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=1023, verbose_name="Название")),
                (
                    "distribution_id",
                    models.CharField(
                        max_length=127,
                        null=True,
                        verbose_name="Прокатное удостоверение",
                    ),
                ),
                (
                    "the_amount_of_the_fee",
                    models.FloatField(verbose_name="Сумма сбора"),
                ),
                (
                    "movie_type",
                    models.CharField(
                        choices=[
                            ("FEAT", "художественный"),
                            ("ANIM", "анимационный"),
                            ("DOCY", "документальный"),
                            ("POPSCI", "научно-популярный"),
                            ("OTHER", "другой"),
                        ],
                        default="OTHER",
                        max_length=127,
                        verbose_name="Тип фильма",
                    ),
                ),
                (
                    "age_limit",
                    models.CharField(
                        max_length=255, verbose_name="Возрастное ограничение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Фильм",
                "verbose_name_plural": "Фильмы",
                "ordering": ["-the_amount_of_the_fee"],
            },
        ),
    ]
