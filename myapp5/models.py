from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)#blank - необязательно для заполнения
    price = models.DecimalField(default=999_999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)#количество, PositiveSmallIntegerField - положительное число целого типа (от 0 до 32 тыс +-)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

    @property
    def total_quantity(selfself):
        return sum(product.quantity for product in Product.objects.all())
