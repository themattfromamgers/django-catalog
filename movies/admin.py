from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'isPublished')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    list_editable = ('isPublished',)
admin.site.register(Movie, MovieAdmin)
