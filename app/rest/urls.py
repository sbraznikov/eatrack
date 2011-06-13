from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView

from app.rest import views

urlpatterns = patterns('',
    # (r'^ingredient/$', ingredient_resource, {'emitter_format': 'json'}),
    # (r'^ingredient/(?P<id>\d+)/$', ingredient_resource, {'emitter_format': 'json'}),
    # (r'^dish/$', dish_resource, {'emitter_format': 'json'}),
    # (r'^dish/(?P<id>\d+)/$', dish_resource, {'emitter_format': 'json'}),
    url(r'^eating/$', views.eating, name='eatracker-eating'),
    url(r'^eating/(?P<id>\w+)/$', views.eating, name='eatracker-eating-id'),
)
