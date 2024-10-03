from django.urls import path
from . import views

app_name = 'onboarding'
urlpatterns = [
    path('images/', views.ImageView.as_view(), name='images')
]