from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamp', 'updated']
    search_fields = ['title']
    raw_id_fields = ['user']

admin.site.register(Article,ArticleAdmin)

