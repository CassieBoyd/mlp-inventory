from django.db import models

class Generation (models.Model):

    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = ("generation")
        verbose_name_plural = ("generations")