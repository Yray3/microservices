from django.db import models
from decimal import Decimal

class Cart(models.Model):
    user_id = models.IntegerField(unique=True)  # ID user from user-service
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for user {self.user_id}"

    @property
    def total_amount(self):
        # total amount
        return sum(item.subtotal for item in self.items.all())

    @property
    def total_items(self):
        # total count
        return sum(item.quantity for item in self.items.all())

    def clear(self):
        # Emptying the cart
        self.items.all().delete()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product_id = models.IntegerField()  # ID order from product-service
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # price when added
    product_name = models.CharField(max_length=200, blank=True)  # Title cache
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['cart', 'product_id']

    def __str__(self):
        return f"{self.quantity}x {self.product_name or f'Product {self.product_id}'}"

    @property
    def subtotal(self):
        return self.price * self.quantity