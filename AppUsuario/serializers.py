from rest_framework import serializers
from django.contrib.auth.models import User

class UsuarioSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = [ 'username', 'email', 'is_staff']