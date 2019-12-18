from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class Feed(APIView) :
    def get(self, request, format=None):
        following_users = request.user.following.all()
        image_list = []

        for following_user in following_users :
            user_image = following_user.images.all()
            for image in user_image :
                image_list.append(image)

        sorted_list = sorted(
            image_list, key=lambda image : image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)
