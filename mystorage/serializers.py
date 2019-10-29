# ModelForm과 유사!

from .models import Essay, Album, Files
from rest_framework import serializers


class EssaySerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Essay
        fields = ("pk", "title", "body", "author")


class AlbumSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")
    image = serializers.ImageField(use_url=True)  # 이미지 결과값을 url로 확인

    class Meta:
        model = Album
        fields = ("pk", "image", "desc", "author")


class FilesSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ("pk", "myfile", "desc", "author")

