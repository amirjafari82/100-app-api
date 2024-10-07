from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('authenticated/', views.IsAuthenticatedView.as_view(), name='is_authenticated'),
]
