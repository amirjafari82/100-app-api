from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('', views.CardView.as_view(), name='card'),
    path('des-card/', views.DesCardView.as_view(), name='des-card')
]
