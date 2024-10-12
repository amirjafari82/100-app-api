from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserLoginSerializer, UserSerializer
from accounts.models import User, Wallet


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            phone = request.data.get('phone')
            user = User.objects.filter(phone=phone)
            ser = UserLoginSerializer(data=request.data)
            if len(user) == 0:
                if ser.is_valid():
                    ser.save()
                    response = super().post(request, *args, **kwargs)
                    tokens = response.data

                    access_token = tokens['access']
                    refresh_token = tokens['refresh']

                    res = Response()

                    res.data = {'message': 'User created', 'data': ser.data}
                    res.set_cookie(key='access_token', value=access_token, httponly=True, secure=True, samesite="None", path="/ ")
                    res.set_cookie(key='refresh_token', value=refresh_token, httponly=True, secure=True, samesite="None", path="/")
                    return res
            else:
                response = super().post(request, *args, **kwargs)
                tokens = response.data
    
                access_token = tokens['access']
                refresh_token = tokens['refresh']
                res = Response()
                user = User.objects.filter(phone=request.data['phone']).first()
                ser_data = UserSerializer(user)
                res.data = {'success': True, 'data': ser_data.data}
                res.set_cookie(key='access_token', value=access_token, httponly=True, secure=True, samesite="None", path="/ ")
                res.set_cookie(key='refresh_token', value=refresh_token, httponly=True, secure=True, samesite="None", path="/")

                return res
            
            
        except:
            return Response({'success': False})


class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            request.data['refresh'] = refresh_token
            
            response = super().post(request, *args, **kwargs)
            
            tokens = response.data
            access_token = tokens['access']
            
            res = Response()
            
            res.data = {'refreshed': True}
            
            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            
            return res
            
        except:
            return Response({'refreshed': False})
    
            
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            res = Response()
            res.data = {'success': True}
            res.delete_cookie('access_token', path='/', samesite='None')
            res.delete_cookie('refresh_token', path='/', samesite='None')
            res.status_code = 200
            return res
        
        except:
            return Response({'success': False})



class IsAuthenticatedView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        user = request.user
        if user.is_anonymous:
            user = {'phone': "", 'first_name': "", 'last_name': "", 'is_admin': ""}
            return Response({'authenticated': False, 'user': user})
        if user.is_authenticated:
            ser_data = UserSerializer(user)
            return Response({'authenticated': True, 'user': ser_data.data, 'balance': user.wallet.balance})