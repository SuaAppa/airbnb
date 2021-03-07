from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models
from users import models as user_models
from rooms import models as room_models


class Review(core_models.TimeStampedModel):
    """Review Model Definition"""
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(user_models.User, on_delete=CASCADE)
    room = models.ForeignKey(room_models.Room, on_delete=CASCADE)
