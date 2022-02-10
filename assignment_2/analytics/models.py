from django.db import models


class Account(models.Model):
    address = models.CharField(max_length=100, null=False, blank=False)
    balance = models.IntegerField()

    def __str__(self):
        return self.address
