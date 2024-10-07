from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.NoteView.as_view(), name='notes')
]