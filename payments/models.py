from django.db import models
# from django.contrib.auth.models import User
from expenses.models import Expenses
from users.models import CustomUser

# Create your models here.


class Payments(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="payments_made"
    )
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="payments_received"
    )
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    user_to_pay_payer = models.ManyToManyField(
        CustomUser, related_name="users_to_pay", blank=True
    )

    def __str__(self):
        return f"{self.amount} paid for {self.expense.title}"
