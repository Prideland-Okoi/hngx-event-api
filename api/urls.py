from django.urls import path, re_path
from . import views

urlpatterns = [
    # User Management
    path('api/users/register/', views.EventUserRegistrationView.as_view(), name='user-registration'),
    path('api/users/login/', views.EventUserLoginView.as_view(), name='user-login'),
    path('api/users/profile/', views.EventUserProfileView.as_view(), name='user-profile'),
    path('api/users/profile/update/', views.EventUserProfileUpdateView.as_view(), name='user-profile-update'),

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
    path('api/groups/', views.EventGroupCreateView.as_view(), name='group-create'),
    path('api/groups/<int:pk>/', views.EventGroupDetailView.as_view(), name='group-detail'),
    path('api/groups/<int:pk>/update/', views.EventGroupUpdateView.as_view(), name='group-update'),
    path('api/groups/<int:pk>/delete/', views.EventGroupDeleteView.as_view(), name='group-delete'),
    path('api/groups/<int:group_id>/members/<int:user_id>/', views.EventGroupAddMemberView.as_view(), name='add-member'),
    path('api/groups/<int:group_id>/members/<int:user_id>/remove/', views.EventGroupRemoveMemberView.as_view(), name='remove-member'),
]
