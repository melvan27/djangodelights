from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class IngredientManager(models.Manager):
    def available(self):
        return self.filter(quantity__gt=0)

class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('kg', _('kilogram'), _('kilograms')),
        ('g', _('gram'), _('grams')),
        ('l', _('liter'), _('liters')),
        ('ml', _('milliliter'), _('milliliters')),
        ('pcs', _('piece'), _('pieces')),
        ('tbsp', _('tablespoon'), _('tablespoons')),
        ('tsp', _('teaspoon'), _('teaspoons')),
        ('cup', _('cup'), _('cups')),
        ('oz', _('ounce'), _('ounces')),
        ('lb', _('pound'), _('pounds')),
        ('pt', _('pint'), _('pints')),
        ('qt', _('quart'), _('quarts')),
        ('gal', _('gallon'), _('gallons')),
        ('fl oz', _('fluid ounce'), _('fluid ounces')),
        ('egg', _('large egg'), _('large eggs')),
        ('pinch', _('pinch'), _('pinches')),
    ]

    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    unit = models.CharField(max_length=10, choices=[(choice[0], choice[2]) for choice in UNIT_CHOICES])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = IngredientManager()

    def __str__(self):
        return self.name

    def get_unit_display(self):
        for choice in self.UNIT_CHOICES:
            if self.unit == choice[0]:
                return choice[2] if self.quantity > 1 else choice[1]
        return self.unit

    def clean(self):
        if self.quantity is not None:
            if self.quantity < 0:
                raise ValidationError(_('Quantity cannot be negative'))

    class Meta:
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")
        ordering = ['name']

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Menu Item")
        verbose_name_plural = _("Menu Items")
        ordering = ['name']

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipe_requirements')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_requirements')
    quantity = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        quantity_str = '{:g}'.format(float(self.quantity))

        if self.ingredient.unit == 'egg':
            unit_display = 'egg' if self.quantity == 1 else 'eggs'
            return f'{quantity_str} {unit_display} for {self.menu_item.name}'
        else:
            return f'{quantity_str} {self.ingredient.unit} of {self.ingredient.name} for {self.menu_item.name}'

    class Meta:
        verbose_name = _("Recipe Requirement")
        verbose_name_plural = _("Recipe Requirements")
        ordering = ['menu_item']

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.IntegerField()
    purchase_time = models.DateTimeField(auto_now_add=True)
    logged_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logged_purchases')

    def __str__(self):
        return f'{self.quantity} {self.menu_item.name} logged by {self.logged_by.username} at {self.purchase_time}'

    def update_inventory(self):
        requirements = self.menu_item.recipe_requirements.all()
        for requirement in requirements:
            ingredient = requirement.ingredient
            required_quantity = requirement.quantity * self.quantity
            if ingredient.quantity < required_quantity:
                raise ValidationError(f'Not enough {ingredient.name} in inventory.')
        
        for requirement in requirements:
            ingredient = requirement.ingredient
            ingredient.quantity -= requirement.quantity * self.quantity
            ingredient.save()

    class Meta:
        verbose_name = _("Purchase")
        verbose_name_plural = _("Purchases")
        ordering = ['-purchase_time']

@receiver(post_save, sender=Purchase)
def update_inventory_on_purchase(sender, instance, **kwargs):
    instance.update_inventory()