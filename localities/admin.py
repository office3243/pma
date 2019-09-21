from django.contrib import admin
from .models import SubLocality, Locality, City, State

admin.site.register(SubLocality)
admin.site.register(Locality)
admin.site.register(City)
admin.site.register(State)
