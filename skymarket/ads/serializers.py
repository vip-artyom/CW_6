from rest_framework import serializers
from ads.models import Ad, Comment
from users.models import User


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdRetrieveSerializer(serializers.ModelSerializer):

    # User information
    phone = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='phone'
    )

    author_first_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='first_name'
    )

    author_last_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='last_name'
    )

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'phone', 'description',
                  'author_first_name', 'author_last_name', 'author_id']


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['image', 'title', 'price', 'description']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):

    # User information
    author_first_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='first_name'
    )

    author_last_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='last_name'
    )

    author_image = serializers.SerializerMethodField('get_author_image_url')

    class Meta:
        model = Comment
        fields = ['pk', 'text', 'created_at',
                  'author_id', 'author_first_name', 'author_last_name',
                  'author_image',
                  'ad_id']

    def get_author_image_url(self, obj):
        request = self.context.get("request")
        image_url = obj.author.image.url if obj.author.image else '/django_media/user_avatars/avatar_placeholder.jpg'
        return request.build_absolute_uri(image_url)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']
