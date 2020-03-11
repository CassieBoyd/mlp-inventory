from django.db import models

class BodyStyle (models.Model):   

    body = models.CharField(max_length=10)
    on_delete = models.DO_NOTHING

    class Meta:
        verbose_name = ("body_style")
        verbose_name_plural = ("body_styles")
