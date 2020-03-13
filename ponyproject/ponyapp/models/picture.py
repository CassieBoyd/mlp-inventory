from django.db import models
from .user_pony import UserPony

class Picture (models.Model):

    img_path = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    user_pony = models.ForeignKey(UserPony, verbose_name=("user_pony"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Picture")
        verbose_name_plural = ("Pictures")