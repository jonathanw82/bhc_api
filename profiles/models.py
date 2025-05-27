from django.db import models
from django.contrib.auth.models import User


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False,
                                  blank=False)
    last_name = models.CharField(max_length=50, null=False,
                                 blank=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    membership_number = models.CharField(max_length=15, unique=True,
                                         blank=True, null=True)
    join_year = models.CharField(max_length=4, blank=True,
                                 null=True)

    def save(self, *args, **kwargs):
        """ Generate the membership number if it doesn't exist. """
        if not self.membership_number:
            self.membership_number = self.generate_membership_number()
        super().save(*args, **kwargs)

    def generate_membership_number(self):
        """Generates a unique membership number."""
        user_count = User_Profile.objects.count()
        return f"{user_count + 1:05d}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
