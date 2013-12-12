from django.conf.urls import patterns, url 

from visualization import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^$', views.collect, name='collect'),
    url(r'^$', views.build, name='build'),
    url(r'^$', views.visualize, name='visualize'),
    url(r'^$', views.findings, name='findings'),
    url(r'^$', views.about, name='about'),
    (r'^test_results/$', views.test_ajax),
)