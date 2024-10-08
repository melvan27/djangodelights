from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm, CustomUserCreationForm, UserProfileForm, CustomPasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import IngredientSerializer, MenuItemSerializer, RecipeRequirementSerializer, PurchaseSerializer
from .permissions import ReadOnlyOrAuthenticated

class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['today_purchases'] = Purchase.objects.filter(purchase_time__date=today)
        context['low_ingredients'] = Ingredient.objects.order_by('quantity')[:5]
        context['menu_items'] = MenuItem.objects.all()
        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class EditProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = 'registration/change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return super().form_valid(form)

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

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [ReadOnlyOrAuthenticated]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ReadOnlyOrAuthenticated]

class RecipeRequirementViewSet(viewsets.ModelViewSet):
    queryset = RecipeRequirement.objects.all()
    serializer_class = RecipeRequirementSerializer
    permission_classes = [ReadOnlyOrAuthenticated]

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [ReadOnlyOrAuthenticated]