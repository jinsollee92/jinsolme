from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {
		'slug': ('title',)
	}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {
		'slug': ('name',)
	}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(File)
# admin.site.register(Post)
# admin.site.register(Category)