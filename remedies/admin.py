from django.contrib import admin
from .models import Remedy, Category, Fitness
# Register your models here.

@admin.register(Remedy)
class RemedyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author',)
    list_filter = ('created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ( 'publish',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Fitness)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name', 'created', 'updated']

    prepopulated_fields = {'slug': ('name',)}