from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('', views.CardView.as_view(), name='card'),
    path('des-card/', views.DesCardView.as_view(), name='des-card'),
    path('transfer/', views.TransferView.as_view(), name='transfer'),
    path('last-sends/', views.LastSendsView.as_view(), name='last-sends'),
    path('transaction/', views.TransactionView.as_view(), name='transaction'),
]
