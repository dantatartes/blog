from django.contrib import admin
from .models import Post


class PublishAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'publish')


admin.site.register(Post, PublishAdmin)
