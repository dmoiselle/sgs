from django.conf.urls import include, url
from django.contrib import admin

#from inventory import views
from sgs import views

admin.site.site_header = 'SGS Shipments'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^shipment/(?P<id>\d+)/', views.shipment_detail, name='shipment_detail'),
    #url(r'^upload/(?P<id>\d+)/', views.upload_detail, name='upload_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
