from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User, Event, Comment, Image, InterestedEvent, Group, UserGroup

# User Management Serializers
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'user_id', 'avatar', 'email')
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'user_id', 'avatar', 'email')

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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

class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name', 'description', 'owner_id')

class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name', 'description')


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User is not active.')
            else:
                raise serializers.ValidationError('Invalid login credentials.')
        else:
            raise serializers.ValidationError('Both username and password are required.')

        return data
