from django.db import models
from skymarket.settings import MEDIA_ROOT
from users.models import CustomUser


class Ad(models.Model):
    title = models.CharField(max_length=256)
    price = models.SmallIntegerField()
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text
