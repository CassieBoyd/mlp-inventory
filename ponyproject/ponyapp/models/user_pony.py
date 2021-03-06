from django.db import models
from .condition import Condition
from django.contrib.auth.models import User
from .pony import Pony

class UserPony (models.Model):

    price = models.DecimalField(decimal_places=2, max_digits=7)
    details = models.CharField(max_length=255)
    timestamp = models.DateTimeField( auto_now=False, auto_now_add=True, null=True)
    condition = models.ForeignKey(Condition, verbose_name=("condition"), on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    pony = models.ForeignKey(Pony, verbose_name=("pony"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("user_pony")
        verbose_name_plural = ("user_ponies")