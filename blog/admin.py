from django.contrib import admin


from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "preview", "creation_date", "is_published", "views_number")
    list_filter = ('is_published', 'creation_date')
    search_fields = ('title', 'content')
