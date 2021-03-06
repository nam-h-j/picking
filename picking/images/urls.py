from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', view=views.Feed.as_view(), name="feed"),
    path('<int:image_id>/like/', view=views.LikeImage.as_view(), name="like_image"),
    path('<int:image_id>/unlike/', view=views.UnLikeImage.as_view(), name="unlike_image"),
    path('<int:image_id>/comment/', view=views.CommentImage.as_view(), name="comment_image"),
    path('comment/<int:comment_id>', view=views.Comment.as_view(), name="comment")
]
