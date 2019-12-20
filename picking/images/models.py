from django.db import models
from picking.users import models as user_models
# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        abstract = True


class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE,related_name='images')

    @property
    def count_likes(self) :
        return self.likes.all().count()

    def __str__(self) :
        return self.caption

    class Meta :
        ordering = ['-created_at']


class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) :
        return self.message


class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='likes')

    def __str__(self) :
        return 'User : {} - Image Caption : {}'.format(self.creator.username, self.image.caption)
