from django.contrib import admin
from .models import Campaign, Size, Entity

admin.site.register(Entity)
admin.site.register(Size)
admin.site.register(Campaign)
