from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cylinder_volume_calculator/', views.cylinder_volume_calculator, name='cylinder_volume_calculator')
]
