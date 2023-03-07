from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def product_quantity(self):
        if self.quantity < 1:
            return 'No Product'
        return self.quantity

    @property
    def rating(self):
        count = self.product_reviews.count()
        if count == 0:
            return 0
        total = 0
        for i in self.product_reviews.all():
            total += i.stars
        return total / count


CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_reviews')

    def __str__(self):
        return self.text


class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Size(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return self.size