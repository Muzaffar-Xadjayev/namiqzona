from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Viloyatlar(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class IqtisodiyZonalar(models.Model):
    region_id = models.ForeignKey(Viloyatlar, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Tashkilotlar(models.Model):
    region_id = models.ForeignKey(Viloyatlar, on_delete=models.CASCADE)
    i_zona = models.ForeignKey(IqtisodiyZonalar, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    date_established = models.DateTimeField()
    director = models.CharField(max_length=150)
    phoneNumber = models.CharField(max_length=200)
    t_address = models.CharField(max_length = 300)
    t_inn = models.IntegerField(default=0)
    t_shxr = models.IntegerField(default=0)
    t_area = models.FloatField(default=0)
    t_investitsiya = models.FloatField(default=0)
    t_xodimlar = models.IntegerField(default=0)
    export = models.FloatField(default=0)
    import_price = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
