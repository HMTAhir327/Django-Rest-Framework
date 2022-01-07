from django.db import models
from rest_framework import serializers
from ..models import WatchList,StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # for getting whole object
    watch_list = WatchListSerializer(many=True,read_only=True)
    # for getting returned string of a model
    # watch_list = serializers.StringRelatedField(many=True)
    # for get url 
    # watch_list = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"


# before implementing model serializer
# validator
# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError('Name is too short')
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # field level validation

#     # def validate_name(self, value):
#     #     if len(value)<2:
#     #         raise serializers.ValidationError('Name is too short')
#     #     else:
#     #         return value

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and description should be different')
#         else:
#             return data

