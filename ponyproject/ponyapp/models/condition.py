from django.db import models

class Condition (models.Model):

    category = models.CharField(max_length=60)
    
    class Meta:
        verbose_name = ("condition")
        verbose_name_plural = ("conditions")