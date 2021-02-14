from django.contrib import admin

from .models import Picture


class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk',)


admin.site.register(Picture, ImageAdmin)
