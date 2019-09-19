from rest_framework import serializers
from .models import Projects, FA


class ProjectSerializer(serializers.ModelSerializer):
    def create(self, validated_records):

        return FA.objects.create(**validated_records)


    def update(self, instance, validated_data):
        instance.save()
        return instance

    class Meta:
        model = Projects
        fields = '__all__'
        # fields = ['name','department']


class FASerializer(serializers.ModelSerializer):

    def create(self, validated_records):

        return FA.objects.create(**validated_records)


    def update(self, instance, validated_data):
        instance.save()
        return instance

    class Meta:
        model = FA
        fields = ['name']

