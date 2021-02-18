from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class post(models.Model):

    class postobjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (('draft','Draft'),('published','Published'))

    category = models.ForeignKey(category, on_delete=models.PROTECT,default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=250,unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager() #default manager
    postobjects = postobjects() #custom manager


    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
    