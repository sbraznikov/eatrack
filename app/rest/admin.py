from django.contrib import admin
from app.rest.models import Nutrients, Category, Ingredient, Dish, Eating


class NutrientsAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('title', 'created_at',)
    ordering = ('-created_at',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('title', 'created_at',)
    ordering = ('-created_at',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('title', 'created_at',)
    ordering = ('-created_at',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


class DishAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('title', 'created_at',)
    ordering = ('-created_at',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


class EatingAdmin(admin.ModelAdmin):
    search_fields = ('eating_type', 'eating_at',)
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('eating_type', 'eating_at',)
    ordering = ('-eating_at',)
    list_filter = ('eating_at',)
    date_hierarchy = 'eating_at'


admin.site.register(Nutrients, NutrientsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Eating, EatingAdmin)

