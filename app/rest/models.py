from django.db import models


class Nutrients(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Ingredient(models.Model):
    nutrients = models.ManyToManyField(Nutrients, blank=True)
    categories = models.ManyToManyField(Category)
    key = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    calorie = models.FloatField()
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Dish(models.Model):
    ingredients = models.ManyToManyField(Ingredient)
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Eating(models.Model):
    EATING_CHOICES = (
        ('1', 'Fruehstueck'),
        ('2', 'Mittagessen'),
        ('3', 'Zwischenmahlzeit'),
        ('4', 'Abendessen'),
    )
    eating_type = models.CharField(max_length=1, choices=EATING_CHOICES)
    comment = models.TextField(blank=True)
    dishes = models.ManyToManyField(Dish)
    eating_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s: %s' % (self.eating_type, self.dishes)
