from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path('', views.index, name="index"),
    path('about/', views.about, name="about"),

    # accounts
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('profile/', views.profile_view, name="profile"),

    # universities
    path('universities/', views.university_list, name="university_list"),
    path('universities/<int:pk>/', views.university_detail, name="university_detail"),

    # calculator
    path('calculator/', views.calculator, name="calculator"),
    path('calculator/result/', views.calculator_result, name="calculator_result"),
]
