from django.db import models
from django.contrib.auth.models import User




#  Chat uchun xonalar yaratish
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# Messeges uchun model
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="message")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added', )