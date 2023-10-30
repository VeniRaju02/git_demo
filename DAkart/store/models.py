from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='images/products')
    stock = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def get_url(self):
        return reverse('products_detail',args=[self.category.url,self.slug])

    def __str__(self):
        return self.product_name
