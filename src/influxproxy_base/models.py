from django.db import models

# Create your models here.

PREFIX_LENGTH=32
PREFIX_DEFAULT='host'


class Client (models.Model):

    name = models.CharField(max_length=32, blank=False, null=False)
    influx_database = models.CharField(max_length=64, blank=False, null=False)
    default_prefix = models.CharField(max_length=PREFIX_LENGTH,
                                      default=PREFIX_DEFAULT)

    def __str__(self):
        return self.name


class ClientUser (models.Model):

    client = models.ForeignKey(Client, null=False)
    name = models.CharField(max_length=32, blank=False, null=False)
    password = models.CharField(max_length=64, blank=False, null=False)
    prefix = models.CharField(max_length=PREFIX_LENGTH, blank=True)

    def __str__(self):
        return self.name
