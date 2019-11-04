from django.contrib import admin
from .models import Reporter, Article

# Register your models here.
admin.site.register(Reporter)
# admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'headline', 'content']
    list_filter = ['pub_date']
    search_fields = ['headline']


admin.site.register(Article, ArticleAdmin)
