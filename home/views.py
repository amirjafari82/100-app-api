from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import AuthenticationFailed
from .serializers import NoteSerializer
from accounts.models import User
from .models import Note

class BankInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):          
        data = [
    {
        "bank": "Markazi",
        "pre-card": "636795"
    },
    {
        "bank": "Melli",
        "pre-card": "603799"
    },
    {
        "bank": "Mellat",
        "pre-card": "610433"
    },
    {
        "bank": "Mellat",
        "pre-card": "991975"
    },
    {
        "bank": "Maskan",
        "pre-card": "628023"
    },
    {
        "bank": "Saderat",
        "pre-card": "603769"
    },
    {
        "bank": "Tose'e Saderat",
        "pre-card": "627648"
    },
    {
        "bank": "Tose'e Saderat",
        "pre-card": "207177"
    },
    {
        "bank": "Sepah",
        "pre-card": "589210"
    },
    {
        "bank": "Tejarat",
        "pre-card": "627353"
    },
    {
        "bank": "Keshavarzi",
        "pre-card": "603770"
    },
    {
        "bank": "Keshavarzi",
        "pre-card": "639217"
    },
    {
        "bank": "Refahe Kargaran",
        "pre-card": "589463"
    },
    {
        "bank": "Ayandeh",
        "pre-card": "636214"
    },
    {
        "bank": "Saman",
        "pre-card": "621986"
    },
    {
        "bank": "Sarmaye",
        "pre-card": "639607"
    },
    {
        "bank": "Sina",
        "pre-card": "639346"
    },
    {
        "bank": "Gardeshgari",
        "pre-card": "505416"
    },
    {
        "bank": "Dey",
        "pre-card": "502938"
    },
    {
        "bank": "Shahr",
        "pre-card": "502806"
    },
    {
        "bank": "Sana'at va Ma'dan",
        "pre-card": "627961"
    },
    {
        "bank": "Iran Zamin",
        "pre-card": "505785"
    },
    {
        "bank": "Pasargad",
        "pre-card": "639347"
    },
    {
        "bank": "Pasargad",
        "pre-card": "502229"
    },
    {
        "bank": "Parsian",
        "pre-card": "622106"
    },
    {
        "bank": "Parsian",
        "pre-card": "639194"
    },
    {
        "bank": "Parsian",
        "pre-card": "627884"
    },
    {
        "bank": "Eghtesade Novin",
        "pre-card": "627412"
    },
    {
        "bank": "Ghavvamin",
        "pre-card": "639599"
    },
    {
        "bank": "Ansar",
        "pre-card": "627381"
    },
    {
        "bank": "Post Iran",
        "pre-card": "627760"
    },
    {
        "bank": "Tose'eh Ta'avon",
        "pre-card": "502908"
    },
    {
        "bank": "Resalat",
        "pre-card": "504172"
    },
    {
        "bank": "KarAfarin",
        "pre-card": "627488"
    },
    {
        "bank": "KarAfarin",
        "pre-card": "502910"
    },
    {
        "bank": "Mehre Eghtesad",
        "pre-card": "639370"
    },
    {
        "bank": "Hekmate Iranian",
        "pre-card": "636949"
    },
]

        return Response(data=data)
        