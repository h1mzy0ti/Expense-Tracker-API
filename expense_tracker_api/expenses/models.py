from django.db import models
from django.contrib.auth.models import User

# Expense model format  (id, amount, category, description, payment_method date, user)

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=255,blank=True)
    payment_method = models.CharField(
        max_length= 20,
        choices=[
            ('cash', 'CASH'),
            ('card', 'CARD'),
            ('upi', 'UPI')
        ],
        default='cash'
    )
