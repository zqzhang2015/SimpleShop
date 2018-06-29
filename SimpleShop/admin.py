from django.contrib import admin
from .models import Product, Order, OrderLine, Client


# Register your models here.
admin.site.register(Product)
admin.site.register(Client)

class OrderLineInline(admin.StackedInline):
    model = OrderLine
    extra = 0
    readonly_fields = ['subtotal']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderLineInline
    ]


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    readonly_fields = ['subtotal']

