from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'unit_price', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(RecipeRequirement)
class RecipeRequirementAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient', 'quantity')
    search_fields = ('menu_item__name', 'ingredient__name')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity', 'purchase_time', 'logged_by')
    search_fields = ('menu_item__name', 'logged_by__username')