from django.urls import path, include
from .views import AutorizeViews

urlpatterns = [
    path('auth/', AutorizeViews.as_view())
]