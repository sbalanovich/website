from django.conf.urls import patterns, url 

from visualization import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^test_results/$', views.test_ajax),
)