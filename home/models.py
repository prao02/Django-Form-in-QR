from django.db import models

# Create your models here.
class form_data(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    mailid = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    class Meta:
        db_table = 'form_data'

    def __str__(self):
        return self.first_name
