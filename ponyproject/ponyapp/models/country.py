from django.db import models

class Country (models.Model):

    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = ("country")
        verbose_name_plural = ("countries")
