from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('edit_excel/', views.edit_excel, name='edit_excel'),
]