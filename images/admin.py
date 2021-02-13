from django.contrib import admin

from .models import Addimage


class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk',)


admin.site.register(Addimage, ImageAdmin)
