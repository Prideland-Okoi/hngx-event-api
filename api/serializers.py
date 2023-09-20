from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import EventUser, Event, Comment, Image, InterestedEvent, EventGroup, UserGroup

# User Management Serializers
class EventUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

class EventUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = ('username', 'user_id', 'avatar', 'email')

class EventUserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = ('username', 'avatar', 'email')

# Event Management Serializers
class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'location', 'start_date', 'end_date', 'start_time', 'end_time', 'thumbnail')

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'location', 'start_date', 'end_date', 'start_time', 'end_time', 'thumbnail')

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body',)

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

# User Interactions Serializers
class InterestedEventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedEvent
        fields = ('user', 'event')

class EventGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGroup
        fields = ('group_name', 'description', 'owner_id')

class EventGroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGroup
        fields = '__all__'

class EventGroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGroup
        fields = ('group_name', 'description')


class EventUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            event_user = authenticate(username=username, password=password)

            if event_user:
                if event_user.is_active:
                    data['event_user'] = event_user
                else:
                    raise serializers.ValidationError('User is not active.')
            else:
                raise serializers.ValidationError('Invalid login credentials.')
        else:
            raise serializers.ValidationError('Both username and password are required.')

        return data
