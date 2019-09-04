from django.contrib import admin
from .models import User

admin.site.site_header = "Printmyad Administration"
admin.site.site_title = "Printmyad Administration"
admin.site.register(User)
