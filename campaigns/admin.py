from django.contrib import admin
from .models import Campaign, Size, Entity, TestModel

admin.site.register(Entity)
admin.site.register(Size)
admin.site.register(Campaign)


"""
    for test purposes.
"""
admin.site.register(TestModel)
