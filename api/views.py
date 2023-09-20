#from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import EventUser, Event, Comment, Image, InterestedEvent, EventGroup, UserGroup

from .serializers import EventUserRegistrationSerializer, EventUserLoginSerializer, EventUserProfileSerializer, EventUserProfileUpdateSerializer
from .serializers import EventCreateSerializer, EventListSerializer, EventDetailSerializer, EventUpdateSerializer
from .serializers import CommentCreateSerializer, ImageListSerializer, InterestedEventCreateSerializer
from .serializers import EventGroupCreateSerializer, EventGroupDetailSerializer, EventGroupUpdateSerializer

# Create your views here.

# User Management Views
class EventUserRegistrationView(generics.CreateAPIView):
    queryset = EventUser.objects.all()
    serializer_class = EventUserRegistrationSerializer

class EventUserLoginView(generics.CreateAPIView):
    serializer_class = EventUserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        event_user = serializer.validated_data['event_user']
        token, _ = Token.objects.get_or_create(event_user=event_user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)

class EventUserProfileView(generics.RetrieveAPIView):
    queryset = EventUser.objects.all()
    serializer_class = EventUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class EventUserProfileUpdateView(generics.UpdateAPIView):
    queryset = EventUser.objects.all()
    serializer_class = EventUserProfileUpdateSerializer
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

class EventGroupCreateView(generics.CreateAPIView):
    queryset = EventGroup.objects.all()
    serializer_class = EventGroupCreateSerializer

class EventGroupDetailView(generics.RetrieveAPIView):
    queryset = EventGroup.objects.all()
    serializer_class = EventGroupDetailSerializer

class EventGroupUpdateView(generics.UpdateAPIView):
    queryset = EventGroup.objects.all()
    serializer_class = EventGroupUpdateSerializer

class EventGroupDeleteView(generics.DestroyAPIView):
    queryset = EventGroup.objects.all()

# Group Add Member View
class EventGroupAddMemberView(generics.CreateAPIView):
    queryset = EventGroup.objects.all()

    def create(self, request, *args, **kwargs):
        # Get the group_id and user_id from the URL parameters
        group_id = kwargs.get('groupId')
        user_id = kwargs.get('userId')

        try:
            event_group = EventGroup.objects.get(pk=group_id)
        except EventGroup.DoesNotExist:
            return Response({'message': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            event_user = EventUser.objects.get(pk=user_id)
        except EventUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is already a member of the group
        if UserGroup.objects.filter(event_group=event_group, event_user=event_user).exists():
            return Response({'message': 'User is already a member of the group'}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the group
        user_group = UserGroup(group=group, user=user)
        user_group.save()

        return Response({'message': 'User added to the group successfully'}, status=status.HTTP_201_CREATED)

# Group Remove Member View
class EventGroupRemoveMemberView(generics.DestroyAPIView):
    queryset = EventGroup.objects.all()

    def destroy(self, request, *args, **kwargs):
        # Get the group_id and user_id from the URL parameters
        group_id = kwargs.get('groupId')
        user_id = kwargs.get('userId')

        try:
            event_group = EventGroup.objects.get(pk=group_id)
        except EventGroup.DoesNotExist:
            return Response({'message': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            event_user = EventUser.objects.get(pk=user_id)
        except EventUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is a member of the group
        try:
            user_group = UserGroup.objects.get(group=group, user=user)
        except UserGroup.DoesNotExist:
            return Response({'message': 'User is not a member of the group'}, status=status.HTTP_404_NOT_FOUND)

        # Remove the user from the group
        user_group.delete()

        return Response({'message': 'User removed from the group successfully'}, status=status.HTTP_204_NO_CONTENT)

