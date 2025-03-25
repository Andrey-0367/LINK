from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'created_at', 'is_published', 'content_preview')
  list_filter = ('is_published', 'created_at')
  search_fields = ('title', 'content')
  list_editable = ('is_published',)
  
  def content_preview(self, obj):
    return mark_safe(obj.content[:100] + '...' if len(obj.content) > 100 else obj.content)
  
  content_preview.short_description = 'Превью содержания'
