from django.contrib import admin
from .models import category, post
# Register your models here.

@admin.register(post)
class siteAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','content','published','slug','author','status']

admin.site.register(category)