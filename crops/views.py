from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions

from .serializers import CategorySerializer, CropSerializer
from .models import Category, Crop


'''
Rest views
'''

class CropList(generics.ListAPIView):

    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class SeasonCrops(generics.ListAPIView):

    serializer_class = CropSerializer

    def get_queryset(self):
        try:
            lookup_kwarg = self.kwargs['name']
            season = Category.objects.get(name=lookup_kwarg)
            return season.crops.all()
        except Exception as e:
            raise exceptions.NotFound


class CropRetrieve(generics.RetrieveAPIView):

    serializer_class = CropSerializer
    queryset = Crop.objects.all();


'''
Django views
'''

class CropDetail(DetailView):

    model = Crop
    template_name = 'crop_details.html'


class BaseView(TemplateView):

    template_name = 'base.html'