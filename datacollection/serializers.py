from rest_framework import serializers
from .models import Dustbin

# Serializers define the API representation.
class DustbinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dustbin
        fields = ['pk','dustbinid','location','level','updated_at']