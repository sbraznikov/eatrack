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
    nutrients = models.ManyToManyField(Nutrients)
    categories = models.ManyToManyField(Category)
    key = models.CharField(max_length=255)
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
        ('1', 'breakfast'),
        ('2', 'lunch'),
        ('3', 'snack'),
        ('4', 'dinner'),
    )
    eating_type = models.CharField(max_length=1, choices=EATING_CHOICES)
    comment = models.TextField(blank=True)
    dishes = models.ManyToManyField(Dish)
    eating_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.eating_type
