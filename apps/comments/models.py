from django.conf import settings
from django.db import models

from apps.tweets.models import Tweet

User = settings.AUTH_USER_MODEL


def comment_image_upload_to(instance, filename):
    return 'comment/{filename}'.format(filename=filename)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True, upload_to=comment_image_upload_to)
    likes = models.ManyToManyField(User, related_name='comment', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
