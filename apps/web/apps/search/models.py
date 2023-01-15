from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'