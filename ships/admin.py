from django.contrib import admin

from ships import models

to_register = [
    models.Ship,
]

admin.site.register(to_register)
