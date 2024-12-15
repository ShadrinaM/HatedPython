from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dancer/<int:pk>/', views.dancer_detail, name='dancer_detail'),
    path('add_dancer/', views.add_dancer, name='add_dancer'),
    path('add-group/', views.add_group, name='add_group'),
    path('add-festival/', views.add_festival, name='add_festival'),
]
