from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.UserView.as_view(), name='users')
]