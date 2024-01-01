from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from users.models import CustomUser

# Create your models here.


class Expenses(models.Model):
    SPLIT_TYPES = [
        ("equal", "Equal Split"),
        # ("all", "Split All"),
        # ('percentage', 'Percentage Split'),
        # ('shares', 'Shares'),
        # Add more choices as needed
    ]
    title = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    payer_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="expenses_paid",
    )
    split_type = models.CharField(max_length=50, choices=SPLIT_TYPES)
    shared_users = models.ManyToManyField(
        CustomUser, related_name="shared_expenses", blank=True
    )
    include_payer = models.BooleanField(default=False)
    user_included = models.BooleanField(default=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Expenses)
def set_payer_and_user_included_on_save(sender, instance, **kwargs):
    """
    Set the payer to the currently logged-in user and user_included flag before saving the Expense instance.
    """
    if not instance.payer:
        # Set the payer only if it's not already set (e.g., when creating a new expense)
        instance.payer = get_user_model().objects.get(id=instance.payer_id)

    # Set user_included flag based on the checkbox value
    if not instance.include_payer:
        instance.user_included = False
