import datetime
from piston.handler import BaseHandler
from piston.utils import rc, throttle
from app.rest.models import Ingredient, Dish, Eating


class IngredientHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    fields = ('id', 'title', 'description',
              'weight', 'calorie', 'key',
              'created_at', 'updated_at')
    model = Ingredient

    def read(self, request, id=None):
        if id:
            return Ingredient.objects.get(pk=id)
        else:
            return Ingredient.objects.all()

    def create(self, request):
        ingredient = Ingredient(
            description=request.POST.get('description'),
            weight=request.POST.get('weight'),
            title=request.POST.get('title'),
            key=request.POST.get('key'),
            calorie=request.POST.get('calorie'),
        )
        ingredient.save()
        return rc.CREATED

    def update(self, request, id):
        try:
            ingredient = Ingredient.objects.get(pk=id)
        except Ingredient.DoesNotExist:
            return rc.NOT_FOUND
        if 'title' in request.POST:
            ingredient.title = request.PUT.get('title')
        if 'description' in request.POST:
            ingredient.description = request.PUT.get('description')
        if 'weight' in request.POST:
            ingredient.weight = request.PUT.get('weight')
        if 'calorie' in request.POST:
            ingredient.calorie = request.PUT.get('calorie')
        if 'key' in request.POST:
            ingredient.key = request.PUT.get('key')
        ingredient.save()
        return ingredient

    def delete(self, request, id):
        try:
            ingredient = Ingredient.objects.get(pk=id)
        except Ingredient.DoesNotExist:
            return rc.NOT_FOUND
        ingredient.delete()
        return rc.DELETED


class DishHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    fields = ('id', 'ingredients', 'key',
              'title', 'description',
              'created_at', 'updated_at')
    model = Dish

    def read(self, request, id=None):
        if id:
            return Dish.objects.get(pk=id)
        else:
            return Dish.objects.all()

    def create(self, request):
        # TODO: rewrite it better!
        dish = Dish(
            key=request.POST.get('key'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        dish.save()
        for ingredient_id in request.POST.getlist('ingredients'):
            ingredient = Ingredient.objects.get(id=ingredient_id)
            dish.ingredients.add(ingredient)
        return rc.CREATED

    def update(self, request, id):
        try:
            dish = Dish.objects.get(pk=id)
        except Ingredient.DoesNotExist:
            return rc.NOT_FOUND
        if 'title' in request.POST:
            dish.title = request.PUT.get('title')
        if 'description' in request.POST:
            dish.description = request.PUT.get('description')
        if 'key' in request.POST:
            dish.key = request.PUT.get('key')
        if 'ingredients' in request.POST:
            dish.ingredients.clear()
            for ingredient_id in request.POST.getlist('ingredients'):
                ingredient = Ingredient.objects.get(id=ingredient_id)
                dish.ingredients.add(ingredient)
        dish.save()
        return dish

    def delete(self, request, id):
        try:
            dish = Dish.objects.get(pk=id)
        except Ingredient.DoesNotExist:
            return rc.NOT_FOUND
        dish.delete()
        return rc.DELETED


class EatingHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    fields = ('id', 'eating_type', 'dishes',
              'eating_at', 'comment', 'created_at',
              'updated_at')
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
