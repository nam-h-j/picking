from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    """ User Model """

    GENDER_CHOICE = {
        ('male','Male'),
        ('female', 'Female'),
        ('not-specified', 'Not Specified')
    }
    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = ImageField(null = True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    website = URLField(null=True)
    bio = TextField(null=True)
    phone = CharField(max_length=140, null=True)
    gender = CharField(max_length=80, choices=GENDER_CHOICE, null=True)
    followers = ManyToManyField("self")
    following = ManyToManyField("self")



    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def post_count(self):
        return self.images.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()
