from django.contrib import admin
from .models import EventUser, Event, Comment, Image, InterestedEvent, EventGroup, UserGroup

# Register your models here.

# Register your models here
@admin.register(EventUser)
class EventUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_id', 'avatar', 'email')
    search_fields = ('username',)
    list_filter = ('username',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'start_date', 'end_date', 'start_time', 'end_time', 'thumbnail')
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'event_user', 'event')
    search_fields = ('body',)
    list_filter = ('event_user', 'event')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'comment', 'image')
    list_filter = ('comment',)

@admin.register(InterestedEvent)
class InterestedEventAdmin(admin.ModelAdmin):
    list_display = ('event_user', 'event')
    list_filter = ('event_user', 'event')

@admin.register(EventGroup)
class EventGroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'group_name', 'description', 'owner_id', 'created_at')
    search_fields = ('group_name',)
    list_filter = ('group_name', 'owner_id')

@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('event_user', 'event_group')
    list_filter = ('event_user', 'event_group')

