from django.contrib import admin
from .models import Magazine, MagazineDay, Guide, DetailGuide
# Register your models here.

admin.site.register(Magazine)
admin.site.register(MagazineDay)
admin.site.register(Guide)
admin.site.register(DetailGuide)
