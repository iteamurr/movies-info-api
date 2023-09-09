import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class MovieType(models.TextChoices):
    FEATURE = "FEAT", _("художественный")
    ANIMATION = "ANIM", _("анимационный")
    DOCUMENTARY = "DOCY", _("документальный")
    POPULAR_SCIENCE = "POPSCI", _("научно-популярный")
    OTHER = "OTHER", _("другой")


class Movie(models.Model):
    movie_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name="Название", max_length=1023)
    distribution_id = models.CharField(
        verbose_name="Прокатное удостоверение", max_length=127, null=True
    )
    the_amount_of_the_fee = models.FloatField(verbose_name="Сумма сбора")
    movie_type = models.CharField(
        verbose_name="Тип фильма",
        choices=MovieType.choices,
        max_length=127,
        default=MovieType.OTHER,
    )
    age_limit = models.CharField(verbose_name="Возрастное ограничение", max_length=255)

    def __repr__(self):
        return f"<Movie {self.name}>"

    def __str__(self):
        return str(self.movie_id)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["-the_amount_of_the_fee"]
