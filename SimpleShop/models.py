from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.CharField(
        'Product ID',
        max_length=128,
        primary_key=True
    )

    name = models.CharField(
        'Product Name',
        max_length=128,
    )

    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    stock = models.IntegerField()

    create_date = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
    )

    modify_date = models.DateField(
        auto_now=True,
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.product_id
