from django.db import models


class Car(models.Model):
    name = models.CharField("Название автомабиля", max_length=30)
