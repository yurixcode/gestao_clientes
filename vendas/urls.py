# Django
from django.urls import path

# Views
from .views import DashboardView

app_name = 'vendas'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dash'),

]
