from django.contrib import admin
from .models import Tags, Image_blog, Blog, Comment


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class Image_blogInline(admin.TabularInline):
    model = Image_blog
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (Image_blogInline,)
    list_display = ('id', 'title', 'created_date')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    search_fields = ('name',)
    list_filter = ('created_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'name', 'created_date')
