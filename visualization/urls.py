from django.conf.urls import patterns, url 

from visualization import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'collect/^$', views.collect, name='collect'),
    url(r'build/^$', views.build, name='build'),
    url(r'visualize^$', views.visualize, name='visualize'),
    url(r'findings/^$', views.findings, name='findings'),
    url(r'about/^$', views.about, name='about'),
    (r'^test_results/$', views.test_ajax),
)