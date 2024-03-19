from django.db import models
from Home.utils import uni_slug_gen

# Create your models here.

class Record(models.Model):
    first_name   = models.CharField(max_length=50, default="")
    last_name    = models.CharField(max_length=50, default="")
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    email    = models.EmailField(max_length=254, unique = True, default="")
    phone    = models.CharField(unique = True, max_length=15, default="")
    address  = models.TextField(default="")
    city     = models.CharField(max_length=50, default="")
    state    = models.CharField(max_length=50, default="")
    zipcode  = models.CharField(max_length=50, default="")
    uni_slug = models.SlugField(unique=True, default="")

    def save(self, *args, **kwargs):
        self.uni_slug = uni_slug_gen(self.first_name)
        super(Record, self).save(args, kwargs)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
