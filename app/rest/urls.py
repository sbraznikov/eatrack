from django.conf.urls.defaults import *

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from app.rest.handlers import IngredientHandler, DishHandler, EatingHandler

ingredient_resource = Resource(handler=IngredientHandler)
dish_resource = Resource(handler=DishHandler)
eating_resource = Resource(handler=EatingHandler)

urlpatterns = patterns('',
    (r'^ingredient/$', ingredient_resource, {'emitter_format': 'json'}),
    (r'^ingredient/(?P<id>\d+)/$', ingredient_resource, {'emitter_format': 'json'}),
    (r'^dish/$', dish_resource, {'emitter_format': 'json'}),
    (r'^dish/(?P<id>\d+)/$', dish_resource, {'emitter_format': 'json'}),
    (r'^eating/$', eating_resource, {'emitter_format': 'json'}),
    (r'^eating/(?P<id>\d+)/$', eating_resource, {'emitter_format': 'json'}),
)
