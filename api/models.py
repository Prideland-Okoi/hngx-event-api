from django.db import models
from tabnanny import verbose
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

# User Model
class EventUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    #access_token = models.CharField(max_length=255)
    #refresh_token = models.CharField(max_length=255)
  
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator_id = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='event_thumbnails/', null=True, blank=True)

    class Meta:
      verbose_name = "Event"
      verbose_name_plural = ("Events")

    def __str__(self):
        return self.title

# Comment Model
class Comment(models.Model):
    body = models.TextField()
    event_user = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.event_user.username} on {self.event.title}'

# Image Model
class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment_images/')

    def __str__(self):
        return f'Image {self.image_id} for Comment {self.comment.id}'

# InterestedEvent Model
class InterestedEvent(models.Model):
    event_user = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.event_user.username} is interested in {self.event.title}'

# Group Model
class EventGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    description = models.TextField()
    owner_id = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

# UserGroup Model
class UserGroup(models.Model):
    event_user = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    event_group = models.ForeignKey(EventGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} is a member of {self.event_group.group_name}'

