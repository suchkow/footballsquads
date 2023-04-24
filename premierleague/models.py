from django.db import models

class ManUtd(models.Model):
    name = models.CharField(max_length=30, blank='false')
    surname = models.CharField(max_length=30)
    age = models.IntegerField(blank='false')
    country = models.CharField(max_length=56)
    market_value = models.IntegerField(blank='true')

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Manchester United'

    def __str__(self):
        return self.name + ' ' + self.surname