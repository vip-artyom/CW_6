from django.db import models
from skymarket.settings import MEDIA_ROOT
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=256, blank=False)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, max_length=4000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(blank=True, max_length=4000)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return self.text
