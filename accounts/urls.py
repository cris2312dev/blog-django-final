from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registro/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('perfil/', views.profile_view, name='profile'),
    path('perfil/editar/', views.profile_edit_view, name='profile_edit'),
    path('usuario/<str:username>/', views.profile_view, name='user_profile'),
]
