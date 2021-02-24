from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#creating model managers to handle prevention and remedy seperately




class Remedy(models.Model):

    #cannonical  url
    def get_absolute_url(self):
        return reverse('remedies:detail', args=[self.slug])

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='remedies')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   


class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title



#fitness model

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('remedies:fitness_list_by_category', args=[self.slug])



class Fitness(models.Model):
    category = models.ForeignKey(Category,
                                related_name='fitnessname',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='fitness',
                                blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name