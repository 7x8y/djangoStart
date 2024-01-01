from django.shortcuts import render
from rest_framework import viewsets

from apis1.models import Company
from apis1.serializers import CompanySerializer


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer