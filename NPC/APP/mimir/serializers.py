from django.contrib.auth.models import User, Group
from rest_framework import serializers
from APP.mimir.models import pttdata
import json
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = pttdata
        fields = ['date', 'author','title','href','pushcount','content']