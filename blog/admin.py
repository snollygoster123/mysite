from django.contrib import admin
from blog.models import Blog, Comment


# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title', 'text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]


admin.site.register(Blog, BlogAdmin)
