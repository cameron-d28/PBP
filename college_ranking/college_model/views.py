from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import College
from .serializers import CollegeSerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
