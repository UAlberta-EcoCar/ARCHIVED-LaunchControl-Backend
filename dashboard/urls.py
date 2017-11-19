from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard_home, name='dashboard_home'),
    url(r'^pipeline/$', views.pipeline_home, name='pipeline_home')
]