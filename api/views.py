#from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User, Event, Comment, Image, InterestedEvent, Group, UserGroup

from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserProfileUpdateSerializer
from .import serializers

# Create your views here.

# User Management Views
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Event Management Views
class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventUpdateView(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventUpdateSerializer

class EventDeleteView(generics.DestroyAPIView):
    queryset = Event.objects.all()

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer

# User Interactions Views
class InterestedEventCreateView(generics.CreateAPIView):
    queryset = InterestedEvent.objects.all()
    serializer_class = InterestedEventCreateSerializer

class InterestedEventDeleteView(generics.DestroyAPIView):
    queryset = InterestedEvent.objects.all()

class GroupCreateView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer

class GroupDetailView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer

class GroupUpdateView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupUpdateSerializer

class GroupDeleteView(generics.DestroyAPIView):
    queryset = Group.objects.all()

# Group Add Member View
class GroupAddMemberView(generics.CreateAPIView):
    queryset = Group.objects.all()

    def create(self, request, *args, **kwargs):
        # Get the group_id and user_id from the URL parameters
        group_id = kwargs.get('groupId')
        user_id = kwargs.get('userId')

        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return Response({'message': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is already a member of the group
        if UserGroup.objects.filter(group=group, user=user).exists():
            return Response({'message': 'User is already a member of the group'}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the group
        user_group = UserGroup(group=group, user=user)
        user_group.save()

        return Response({'message': 'User added to the group successfully'}, status=status.HTTP_201_CREATED)

# Group Remove Member View
class GroupRemoveMemberView(generics.DestroyAPIView):
    queryset = Group.objects.all()

    def destroy(self, request, *args, **kwargs):
        # Get the group_id and user_id from the URL parameters
        group_id = kwargs.get('groupId')
        user_id = kwargs.get('userId')

        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return Response({'message': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is a member of the group
        try:
            user_group = UserGroup.objects.get(group=group, user=user)
        except UserGroup.DoesNotExist:
            return Response({'message': 'User is not a member of the group'}, status=status.HTTP_404_NOT_FOUND)

        # Remove the user from the group
        user_group.delete()

        return Response({'message': 'User removed from the group successfully'}, status=status.HTTP_204_NO_CONTENT)

