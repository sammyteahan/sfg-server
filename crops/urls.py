from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(r'crops/$', views.CropList.as_view(), name='crop-list'),
    url(r'crops/(?P<pk>[\d]+)$', views.CropRetrieve.as_view(), name='crop-retrieve'),
    url(r'crop/(?P<pk>[\d]+)$', views.CropDetail.as_view(), name='crop-detail'),
    url(r'season/(?P<name>[\w]+)$', views.SeasonCrops.as_view(), name='season-crops'),
)