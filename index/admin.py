from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Images
#model admin options
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","id",]
    #list_display_links = ["updated"]


    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)

class ImageModelAdmin(admin.ModelAdmin):
    list_display = ["image","post","id",]
    #list_display_links = ["updated"]


    class Meta:
        model = Images
admin.site.register(Images, ImageModelAdmin)
