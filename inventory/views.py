from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['today_purchases'] = Purchase.objects.filter(purchase_time__date=today)
        context['low_ingredients'] = Ingredient.objects.order_by('quantity')[:5]
        context['menu_items'] = MenuItem.objects.all()
        return context

class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient-list')

class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'inventory/menu_list.html'
    context_object_name = 'menu_items'

class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    context_object_name = 'purchases'

class ProfitAndRevenueView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/profit_and_revenue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = Purchase.objects.all()
        total_revenue = sum(purchase.menu_item.price * purchase.quantity for purchase in purchases)
        total_cost = sum(
            requirement.ingredient.unit_price * requirement.quantity * purchase.quantity
            for purchase in purchases
            for requirement in purchase.menu_item.recipe_requirements.all()
        )
        context['total_revenue'] = total_revenue
        context['total_cost'] = total_cost
        context['profit'] = total_revenue - total_cost
        return context

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/add_ingredient.html'
    success_url = reverse_lazy('ingredient-list')

class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/add_menu_item.html'
    success_url = reverse_lazy('menu-list')

class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'inventory/add_recipe_requirement.html'
    success_url = reverse_lazy('menu-list')

    def get_initial(self):
        initial = super().get_initial()
        menu_item_id = self.request.GET.get('menu_item')
        if menu_item_id:
            menu_item = get_object_or_404(MenuItem, id=menu_item_id)
            initial['menu_item'] = menu_item
        return initial

class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/record_purchase.html'
    success_url = reverse_lazy('purchase-list')

    def form_valid(self, form):
        form.instance.logged_by = self.request.user
        return super().form_valid(form)

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/update_ingredient.html'
    success_url = reverse_lazy('ingredient-list')