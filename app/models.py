from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Model"
        verbose_name = "User Model"
        verbose_name_plural = "User Model"
