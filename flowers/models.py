from django.db import models


class Shop(models.Model):
    city = models.TextField(blank=True, null=True)
    house = models.TextField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    office_hours = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'shop'

class Plant(models.Model):
    description = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    species = models.TextField()
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'plant'

