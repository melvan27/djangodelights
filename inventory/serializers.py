from rest_framework import serializers
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['url', 'name', 'quantity', 'unit', 'unit_price']

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['url', 'name', 'price', 'image_url']

class RecipeRequirementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecipeRequirement
        fields = ['url', 'menu_item', 'ingredient', 'quantity']

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase
        fields = ['url', 'menu_item', 'quantity']