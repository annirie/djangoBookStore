from django.contrib.auth.models import AbstractUser
from django.db import models


# CustomUser inherits all functionality of AbstractUser and extensions would be added later
class CustomUser(AbstractUser):
    pass
