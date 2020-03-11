from django.db import models
from .condition import Condition
from django.contrib.auth.models import User
from .pony import Pony

class UserPony (models.Model):

    price = models.DecimalField()
    details = models.CharField(max_length=255)
    timestamp = models.DateTimeField( auto_now=False, auto_now_add=True)
    condition = models.ForeignKey(Condition, verbose_name=("condition"), on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    pony = models.ForeignKey(Pony, verbose_name=_("pony"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("user_pony")
        verbose_name_plural = ("user_ponies")