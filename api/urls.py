from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^v(?P<version>[0-9]+)/pipeline/$', views.DataEventAPI.as_view(), name='Data_Event_API'),
]
