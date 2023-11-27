from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class pttdata(models.Model):
    date = models.TextField()
    author = models.TextField()
    title = models.TextField()
    href = models.TextField()
    pushcount = models.TextField()
    content = models.TextField()
class Meta:
        db_table = "PTT_NEWS"