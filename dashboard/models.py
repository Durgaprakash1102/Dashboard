from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('team_1', 'Team 1'),
        ('team_2', 'Team 2'),
        ('team_3', 'Team 3'),
        ('team_4', 'Team 4'),
        ('super_admin', 'Super Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    original_password = models.CharField(max_length=255, blank=False, null=True)  # For storing original passwords temporarily


from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.TextField()
    is_interested = models.BooleanField(blank=True,null=True)
    is_not_interested = models.BooleanField(blank=True,null=True)
    is_eligible = models.BooleanField(blank=True,null=True)
    is_not_eligible = models.BooleanField(blank=True,null=True)
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from datetime import date, timedelta


class Loan(models.Model):
    class LoanStatus(models.TextChoices):
        CLEARED = 'CLEARED', 'Cleared'
        PENDING = 'PENDING', 'Pending'
        DEFAULTED = 'DEFAULTED', 'Defaulted'

    class CriticalStatus(models.TextChoices):
        NORMAL = 'NORMAL', 'Normal'
        CRITICAL = 'CRITICAL', 'Critical'

    name = models.CharField(max_length=255)
    loan_id = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    present_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenure = models.PositiveIntegerField(help_text="Loan tenure in months")
    total_monthly_emi_amount = models.DecimalField(max_digits=10, decimal_places=2)
    emi_due_date = models.DateField()
    emi_cleared = models.BooleanField(default=False)
    extended_due_date = models.DateField(null=True, blank=True)
    critical_loan_status = models.CharField(
        max_length=10,
        choices=CriticalStatus.choices,
        default=CriticalStatus.NORMAL
    )
    visit_date = models.DateField(null=True, blank=True)
    visit_remarks=models.TextField(null=True,blank=True)
    revisit_date = models.DateField(null=True, blank=True)

    revisit_reason = models.TextField(null=True, blank=True)
    due_date_pending_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - Loan ID: {self.loan_id}"

    def check_and_update_critical_status(self):
        today = date.today()

        due_date = self.extended_due_date if self.extended_due_date else self.emi_due_date

        if not isinstance(due_date, date):
            due_date = date.fromisoformat(due_date)

        if not self.emi_cleared and today > due_date + timedelta(days=60):
            self.critical_loan_status = self.CriticalStatus.CRITICAL
        else:
            self.critical_loan_status = self.CriticalStatus.NORMAL

        self.save()
