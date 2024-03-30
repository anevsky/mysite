from django.db import models
from django.forms import ModelForm


class User(models.Model):
    ADMIN = "ADMIN"
    REGULAR = "REGULAR"
    ROLES = {
        ADMIN: "Admin - Can delete members",
        REGULAR: "Regular - Can't delete members"
    }

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ROLES, default=REGULAR)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone", "role"]