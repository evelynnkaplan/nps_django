from nps_django.models import Passholder, Pass, Park, Visit
from rest_framework import serializers

class PassholderSerializer(serializers.HyperlinkedModelSerializer):
  passes = serializers.StringRelatedField(many=True)
  visits = serializers.StringRelatedField(many=True)

  class Meta:
    model = Passholder
    fields = ('first_name', 'last_name', 'passes', 'visits')

class PassSerializer(serializers.HyperlinkedModelSerializer):
  passholder_primary = serializers.StringRelatedField()

  class Meta:
    model = Pass
    fields = ('pass_id', 'type', 'passholder_primary', 'passholder_secondary', 'expiration_date', 'zip_code', 'email', 'phone_num', 'cost')

class ParkSerializer(serializers.HyperlinkedModelSerializer):
  visits = serializers.StringRelatedField(many=True)

  class Meta:
    model = Park
    fields = ('name', 'state', 'visits')

class VisitSerializer(serializers.HyperlinkedModelSerializer):
  park_queryset = Park.objects.all()
  passholder_queryset = Passholder.objects.all()
  
  park = serializers.PrimaryKeyRelatedField(queryset = park_queryset)
  passholder = serializers.PrimaryKeyRelatedField(queryset = passholder_queryset)

  class Meta:
    model = Visit
    fields = ('park', 'passholder', 'date')