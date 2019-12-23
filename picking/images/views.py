from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class Feed(APIView) :
    def get(self, request, format=None) :
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

class LikeImage(APIView) :
    def get(self, request, id, format=None) :

        try :
            get_image = models.Image.objects.get(id=id)
        except models.Image.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)

        try :
            check_like = models.Like.objects.get(
                creator = request.user,
                image = get_image
            )
            check_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Like.DoesNotExist :
            new_like = models.Like.objects.create(
                creator = request.user,
                image = get_image
            )
            new_like.save()
            return Response(status=status.HTTP_201_CREATED)
