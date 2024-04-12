from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']
    
admin.site.unregister(Comment)  
admin.site.register(Comment, CommentAdmin) 






