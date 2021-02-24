from django.db import models

from customer.models import Customer


class CustomProduct(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.product_name}: {self.price}"

    class Meta:
        db_table = 'custom_products'


class NonCustomProducts(models.Model):
    p_id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.product_name}: {self.price}"

    class Meta:
        db_table = 'non_custom_products'


class OrderStatus(models.Model):
    status_id = models.BigIntegerField(primary_key=True)
    paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'order_status'


class Order(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    order_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, to_field='customer_id', on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(OrderStatus, to_field='status_id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.order_number}: {self.status_id}"

    class Meta:
        db_table = 'orders'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, to_field='order_id', on_delete=models.CASCADE)
    product = models.ForeignKey(CustomProduct, to_field='product_id', on_delete=models.SET_NULL, null=True)
    p = models.ForeignKey(NonCustomProducts, to_field='p_id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.order}: {self.product}"

    class Meta:
        db_table = 'order_items'
