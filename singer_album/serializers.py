from rest_framework import serializers

from singer_album.models import Singer, Album


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('id',
                  'name',
                  'age',
                  'achievement')


class AlbumSerializer(serializers.ModelSerializer):
    singer = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id',
                  'name',
                  'date_published',
                  'singer')
