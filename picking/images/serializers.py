from rest_framework import serializers
from . import models
from picking.users import models as user_models

class UserProfileImageSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Image
        fields = (
            'id',
            'file',
            'count_likes',
            'count_comment',
        )

class FeedUserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = user_models.User
        fields = (
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer) :
    creator = FeedUserSerializer(read_only=True)
    class Meta :
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        )

class LikeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = models.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer) :
    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()
    class Meta :
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'count_likes',
            'creator'
        )
