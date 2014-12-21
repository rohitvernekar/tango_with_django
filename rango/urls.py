from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^index/$',views.index),
        url(r'^about/$',views.about),
        url(r'^category/(?P<category_name_url>\w+)/$', views.category,name='category'),
    )
