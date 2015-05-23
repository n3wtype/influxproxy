from django.contrib import admin
from influxproxy_base.models import Client, ClientUser

# Register your models here.

admin.site.register(Client)
admin.site.register(ClientUser)

