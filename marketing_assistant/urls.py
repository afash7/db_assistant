from django.urls import path
from main import views

urlpatterns = [
    path('read_excel/', views.read_excel, name='read_excel'),
    path('edit_excel/', views.edit_excel, name='edit_excel'),
]