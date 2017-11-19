from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard_home, name='dashboard_home'),
    url(r'^new/$', views.new_dashboard, name='new_dashboard'),
    url(r'^pipeline/$', views.pipeline_home, name='pipeline_home'),
    url(r'^(?P<pk>\d+)/$', views.dashboard, name='dashboard'),
    url(r'^chart/new/$', views.new_chart, name="new_chart"),
]