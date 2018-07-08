from django.db import models


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


class Client(models.Model):
    first_name = models.CharField(
        'First Name',
        max_length=128,
    )

    last_name = models.CharField(
        'Last Name',
        max_length=128,
    )

    email_address = models.EmailField(
        'Email Address',
    )

    def __str__(self):
        return self.email_address


class Order(models.Model):

    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True
    )

    po_number = models.CharField(
        max_length=64,
        blank=False,
        unique=True,
    )

    ORDER_STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Done', 'Done'),
    )

    order_status = models.CharField(
        max_length=24,
        choices=ORDER_STATUS_CHOICES,
        default='Open',
    )

    create_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )

    modify_date = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.po_number


class OrderLine(models.Model):
    # Each line of the order, which will consist of product, quantity, etc. One product per OrderItem.
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders',
    )

    item = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='item'
    )

    quantity = models.IntegerField(    )

    @property
    def subtotal(self):
        return self.item.sale_price * self.quantity

    def __str__(self):
        return '{} - {}'.format(self.order.po_number, self.id)


class ContactMessage(models.Model):

    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
    )

    recipient_email = models.EmailField(
        'Recipient Email',
    )

    subject = models.CharField(
        'Subject',
        max_length=200,
    )

    body = models.TextField(
        'Email Body',
        max_length=1000,
    )

    add_comments = models.TextField(
        'Additional Comments',
        max_length=1000,
        blank=True,
        null=True,
    )

    @property
    def client_name(self):
        return '{} {}'.format(self.client.first_name, self.client.last_name)
