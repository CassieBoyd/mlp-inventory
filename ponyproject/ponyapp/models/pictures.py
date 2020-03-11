from django.db import models
from 

class Picture (models.Model):

    img_path = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    user_pony = models.ForeignKey()

    class Meta:
        verbose_name = ("Picture")
        verbose_name_plural = ("Pictures")