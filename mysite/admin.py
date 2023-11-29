from django.contrib import admin
from mysite.models import Post, Product, Comments
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','pub_date')
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentAdmin)
