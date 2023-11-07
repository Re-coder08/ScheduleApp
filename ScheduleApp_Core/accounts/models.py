from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTOMER = "CUSTOMER", "Customer"
        STAFF = "STAFF", "Staff"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


#----- Customer Models -------

class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)


class Customer(User):

    base_role = User.Role.CUSTOMER

    student = CustomerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Customers"


@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.IntegerField(null=True, blank=True)


# ------- End of Customer Models -------


# ------- Staff Models ----------

class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STAFF)


class Staff(User):

    base_role = User.Role.STAFF

    teacher = StaffManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Staff"


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.IntegerField()
    staff_start_time = models.TimeField(null=True, blank=True)
    staff_end_time = models.TimeField(null=True, blank=True)



@receiver(post_save, sender=Staff)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STAFF":
        StaffProfile.objects.create(user=instance)


# ------- End of Staff Models --------