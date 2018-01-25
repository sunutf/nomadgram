from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram.users import models as user_models
from nomadgram.images import models as image_models


class Notification(image_models.TimeStampedModel):

    #1st index 는 데이터베이스, 2nd는 어드민 패널, api 에서 보는거
    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow','Follow')
        )

    creator = models.ForeignKey(user_models.User, related_name='creator')
    to = models.ForeignKey(user_models.User, related_name='to')
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    images = models.ForeignKey(image_models.Image, null=True, blank=True)