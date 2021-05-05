from rest_framework import serializers
from . import models


class ProductSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'user', 'title', 'quantity')
