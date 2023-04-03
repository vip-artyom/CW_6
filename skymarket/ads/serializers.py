from rest_framework import serializers
from ads.models import Ad, Comment


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    phone = serializers.CharField(source='author.phone', read_only=True)

    class Meta:
        model = Ad
        fields = ['pk', 'title', 'price', 'author', 'author_first_name', 'image', 'description', 'phone']


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['image', 'title', 'price', 'description']


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    ad_id = serializers.IntegerField(source='ad.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['pk', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name', 'ad_id',
                  'author_image']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']
