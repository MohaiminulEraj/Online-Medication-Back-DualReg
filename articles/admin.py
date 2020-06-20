from django.contrib import admin
from .models import PostedArticle


class PostedArticleAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'title', 'topic',
                    'symptomps', 'created', 'datecompleted')
    search_fields = ('title', 'topic', 'symptomps')
    readonly_fields = ('created',)


admin.site.register(PostedArticle, PostedArticleAdmin)
