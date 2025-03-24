from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('details/<int:d>', views.details, name='details')
]