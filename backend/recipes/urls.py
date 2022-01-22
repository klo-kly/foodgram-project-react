from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import IngredientViewSet, RecipeViewSet, TagViewSet

router_v0 = DefaultRouter()
router_v0.register('tags', TagViewSet, basename='tags')
router_v0.register('ingredients', IngredientViewSet, basename='ingredients')
router_v0.register('recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('', include(router_v0.urls)),
]