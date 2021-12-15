from django.contrib import admin
# ここから下に貼り付けてください
from company.models import Pokemon, Type

admin.site.register(Pokemon)
admin.site.register(Type)