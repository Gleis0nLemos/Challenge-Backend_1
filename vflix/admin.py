from django.contrib import admin
from vflix.models import Video

class Videos(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'url')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description', 'url')
    list_per_page = 20

admin.site.register(Video, Videos)