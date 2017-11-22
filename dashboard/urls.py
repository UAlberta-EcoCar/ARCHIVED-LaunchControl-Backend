from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard_home, name='dashboard_home'),
    url(r'^new/$', views.new_dashboard, name='new_dashboard'),
    url(r'^api/$', views.api_dashboard, name='api_dashboard'),
    url(r'^pipeline/(?P<pk>\d+)/$', views.pipeline_home, name='pipeline_home'),
    url(r'^(?P<pk>\d+)/$', views.dashboard, name='dashboard'),
    url(r'^(?P<pk>\d+)/edit/$', views.dashboard_edit, name='dashboard_edit'),
    url(r'^chart/(?P<pk>\d+)/$', views.chart, name="chart"),
    url(r'^chart/(?P<pk>\d+)/edit/$', views.chart_edit, name="chart_edit"),
    url(r'^chart/new/$', views.new_chart, name="new_chart"),
    url(r'^pipeline/new/$', views.new_pipeline, name='new_pipeline'),
    url(r'^datapointtype/new/$', views.new_datapointtype, name='new_datapointtype'),
    url(r'^pipeline/(?P<pk>\d+)/edit/$', views.pipeline_edit, name='pipeline_edit'),
    url(r'^datapointtype/(?P<pk>\d+)/$', views.datapointtype, name="datapointtype"),
    url(r'^datapointtype/(?P<pk>\d+)/edit/$', views.datapointtype_edit, name="datapointtype_edit"),
]