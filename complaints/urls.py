from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^engineers/$', views.engineers, name='engineers'),
    url(r'^engineers/(?P<engineer_id>[0-9]+)/$', views.engineer_details, name='engineer_details'),
    url(r'^complaints/$', views.complaints, name='complaints'),
    url(r'^complaints/(?P<complaint_id>[0-9]+)/$', views.complaint_details, name='complaint_details'),
    # ex: /polls/5/results/
]