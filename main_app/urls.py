from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('ninjas/', views.ninja_index, name='ninja-index'),
    path('ninjas/<int:ninja_id>/', views.ninja_detail, name='ninja-detail'),
    path('ninjas/create/', views.NinjaCreate.as_view(), name='ninja-create'),
    path('ninjas/<int:pk>/update/', views.NinjaUpdate.as_view(), name='ninja-update'),
    path('ninjas/<int:pk>/delete/', views.NinjaDelete.as_view(), name='ninja-delete'),
   
    path('weapons/create/', views.WeaponCreate.as_view(), name='weapon-create'),
    path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapon-detail'),
    path('weapons/', views.WeaponList.as_view(), name='weapon-index'),
    path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapon-update'),
    path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapon-delete'),
    path('ninjas/<int:ninja_id>/associate-weapon/<int:weapon_id>/', views.associate_weapon, name='associate-weapon'),
    path('ninjas/<int:ninja_id>/remove-weapon/<int:toweapon_id>/', views.remove_weapon, name='remove-weapon'),
    path('accounts/signup/', views.signup, name='signup'),

]
