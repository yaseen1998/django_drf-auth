from django.db.models import fields
from rest_framework import serializers
from .models import Add_data
class AddSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','anime_name','anime_type','anime_desc','anime_rank','anime_watcher','anime_country')
        model = Add_data