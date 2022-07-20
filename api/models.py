from django.db import models

# Create your models here.
class MyUser(models.Model):
    first_name = models. CharField(max_length=50)
    last_name = models. CharField(max_length=50)
    company_name = models. CharField(max_length=50)
    age = models.IntegerField()
    city = models. CharField(max_length=50)
    state = models. CharField(max_length=50)
    zip = models.IntegerField()
    email = models. EmailField()
    web = models.URLField()

    def __str__(self):
        return str(self.id)