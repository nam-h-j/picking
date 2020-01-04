from rest_framework import serializers
from . import models
from picking.images import serializers as image_seriallizers

class ExploreUserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name'
        )

class UserProfileSerializer(serializers.ModelSerializer):
    images = image_seriallizers.UserProfileImageSerializer(many=True)
    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images',
        )
