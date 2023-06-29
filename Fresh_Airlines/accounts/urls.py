from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
]


