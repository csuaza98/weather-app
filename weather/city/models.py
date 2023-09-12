from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="name")
    flag = models.CharField(max_length=500, verbose_name="flag", null=True)

    class Meta:
        ordering = ['id']
