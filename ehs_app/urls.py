
from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.profile_list, name='profile-list'),
    path('profiles/<int:pk>/', views.profile_detail, name='profile-detail'),
]
