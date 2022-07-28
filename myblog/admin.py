from django.contrib import admin

from myblog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'post', 'text', 'created_date')
    list_filter = ('username', 'created_date')
    search_fields = ('username', 'text')

admin.site.register(Comment, CommentAdmin)

