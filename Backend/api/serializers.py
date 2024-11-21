from rest_framework import serializers
from .models import DatabaseConfig


class DatabaseConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseConfig
        fields = ['host', 'port', 'namedb', 'user', 'password', 'query']