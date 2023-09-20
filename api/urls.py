from django.urls import path, re_path
from . import views

urlpatterns = [
    # User Management
    path('api/users/register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('api/users/login/', views.UserLoginView.as_view(), name='user-login'),
    path('api/users/profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('api/users/profile/update/', views.UserProfileUpdateView.as_view(), name='user-profile-update'),

    # Event Management
    path('api/events/', views.EventListView.as_view(), name='event-list'),
    path('api/events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('api/events/create/', views.EventCreateView.as_view(), name='event-create'),
    path('api/events/update/<int:pk>/', views.EventUpdateView.as_view(), name='event-update'),
    path('api/events/delete/<int:pk>/', views.EventDeleteView.as_view(), name='event-delete'),
    path('api/events/<int:event_id>/comments/', views.CommentCreateView.as_view(), name='comment-create'),
    path('api/comments/<int:comment_id>/images/', views.ImageListView.as_view(), name='image-list'),

    # User Interactions
    path('api/users/<int:user_id>/interests/<int:event_id>/', views.InterestedEventCreateView.as_view(), name='express-interest'),
    path('api/users/<int:user_id>/interests/<int:event_id>/remove/', views.InterestedEventDeleteView.as_view(), name='remove-interest'),
    path('api/groups/', views.GroupCreateView.as_view(), name='group-create'),
    path('api/groups/<int:pk>/', views.GroupDetailView.as_view(), name='group-detail'),
    path('api/groups/<int:pk>/update/', views.GroupUpdateView.as_view(), name='group-update'),
    path('api/groups/<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group-delete'),
    path('api/groups/<int:group_id>/members/<int:user_id>/', views.GroupAddMemberView.as_view(), name='add-member'),
    path('api/groups/<int:group_id>/members/<int:user_id>/remove/', views.GroupRemoveMemberView.as_view(), name='remove-member'),
]
