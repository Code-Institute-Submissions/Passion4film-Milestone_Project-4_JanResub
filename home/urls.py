from django.urls import path
from . import views


urlpatterns = [
    path('health_benefits/', views.health_benefits,
         name='health_benefits'),
    path('', views.index, name='home'),
]
