import datetime
from piston.handler import BaseHandler
from piston.utils import rc, throttle
from app.rest.models import Ingredient, Dish, Eating


class EatingHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    fields = ('_id', 'type', 'dishes',
              'date', 'comment', 'created_at')
    model = Eating

    def read(self, request, id=None):
        if id:
            return Eating.objects.get(pk=id)
        else:
            return Eating.objects.all()

    def create(self, request):
        eating = Eating(
            eating_type=request.POST.get('eating_type'),
            comment=request.POST.get('comment', ''),
            eating_at=request.POST.get('eating_at', datetime.datetime.now())
         )
        eating.save()
        for key in request.POST.getlist('dishes'):
            dish = Dish.objects.get(key=key)
            eating.dishes.add(dish)
        return rc.CREATED

    def update(self, request, id):
        try:
            eating = Eating.objects.get(pk=id)
        except Ingredient.DoesNotExist:
            return rc.NOT_FOUND
        if 'eating_type' in request.POST:
            eating.eating_type = request.PUT.get('eating_type')
        if 'eating_at' in request.POST:
            eating.eating_at = request.PUT.get('eating_at')
        if 'comment' in request.POST:
            eating.comment = request.PUT.get('comment')
        if 'dishes' in request.POST:
            eating.dishes.clear()
            for key in request.POST.getlist('dishes'):
                dish = Dish.objects.get(key=key)
                eating.dishes.add(dish)
        eating.save()
        return eating

    def delete(self, request, id):
        try:
            eating = Eating.objects.get(pk=id)
        except Ingredient.DoesNotExist:
            return rc.NOT_FOUND
        eating.delete()
        return rc.DELETED
