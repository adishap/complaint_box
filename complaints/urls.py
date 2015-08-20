from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_complaint/$', views.add_complaint, name='add_complaint'),
    url(r'^engineers/$', views.engineers, name='engineers'),
    url(r'^engineers/(?P<engineer_id>[0-9]+)/$', views.engineer_details, name='engineer_details'),
    url(r'^complaints/$', views.complaints, name='complaints'),
    url(r'^complaints/(?P<complaint_id>[0-9]+)/$', views.complaint_details, name='complaint_details'),
 	url(r'^complaints/(?P<complaint_id>[0-9]+)/complaint_update/$', views.complaint_update, name='complaint_update'),   
    url(r'^amc_clients/$', views.amc_clients, name='amc_clients'),
    url(r'^amc_clients/(?P<amc_id>[0-9]+)/$', views.amc_details, name='amc_details'),
]