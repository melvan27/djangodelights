from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IngredientListView, IngredientDeleteView, MenuItemListView,
    PurchaseListView, ProfitAndRevenueView, IngredientCreateView,
    MenuItemCreateView, RecipeRequirementCreateView, PurchaseCreateView,
    IngredientUpdateView, HomePageView, IngredientViewSet, MenuItemViewSet,
    RecipeRequirementViewSet, PurchaseViewSet
)

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'recipe-requirements', RecipeRequirementViewSet)
router.register(r'purchases', PurchaseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', HomePageView.as_view(), name='home'),
    path('ingredients/', IngredientListView.as_view(), name='ingredient-list'),
    path('ingredients/delete/<int:pk>/', IngredientDeleteView.as_view(), name='ingredient-delete'),
    path('ingredients/add/', IngredientCreateView.as_view(), name='ingredient-add'),
    path('ingredients/update/<int:pk>/', IngredientUpdateView.as_view(), name='ingredient-update'),
    path('menu/', MenuItemListView.as_view(), name='menu-list'),
    path('menu/add/', MenuItemCreateView.as_view(), name='menu-add'),
    path('menu/recipe/add/', RecipeRequirementCreateView.as_view(), name='recipe-requirement-add'),
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('purchases/add/', PurchaseCreateView.as_view(), name='purchase-add'),
    path('profit-and-revenue/', ProfitAndRevenueView.as_view(), name='profit-and-revenue'),
]