from django.db import models
from .country import Country


class Pony (models.Model):

    name = models.CharField(max_length=80)
    year = models.IntegerField(max_length=4)
    hair_color = models.CharField(max_length=80)
    body_color = models.CharField(max_length=80)
    country = models.ForeignKey(Country, verbose_name=("Country"), on_delete=models.DO_NOTHING)
    body_style = models.ForeignKey(BodyStyle, verbose_name=("body_style"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("pony")
        verbose_name_plural = ("ponies")