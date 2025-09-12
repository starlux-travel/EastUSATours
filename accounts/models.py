from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("姓名", max_length=100, blank=True)
    mobile = models.CharField("手機", max_length=20, blank=True)

    def __str__(self):
        return self.full_name or self.user.username
