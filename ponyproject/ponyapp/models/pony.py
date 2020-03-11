from django.db import models
from .country import Country
from .body_style import BodyStyle
from .generation import Generation

class Pony (models.Model):

    name = models.CharField(max_length=80)
    year = models.IntegerField(max_length=4)
    hair_color = models.CharField(max_length=80)
    body_color = models.CharField(max_length=80)
    img_path = models.CharField(max_length=255)
    country = models.ForeignKey(Country, verbose_name=("Country"), on_delete=models.DO_NOTHING)
    body_style = models.ForeignKey(BodyStyle, verbose_name=("body_style"), on_delete=models.DO_NOTHING)
    generation = models.ForeignKey(Generation, verbose_name=("generation"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("pony")
        verbose_name_plural = ("ponies")