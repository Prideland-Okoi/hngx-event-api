### Documentation for Event Management System API

This API is built using Django REST Framework and provides the following endpoints:

**User Management**

* **Register:** `/api/users/register/`
* **Login:** `/api/users/login/`
* **Get Profile:** `/api/users/profile/`
* **Update Profile:** `/api/users/profile/update/`

**Event Management**

* **List Events:** `/api/events/`
* **Get Event Details:** `/api/events/<int:pk>/`
* **Create Event:** `/api/events/create/`
* **Update Event:** `/api/events/update/<int:pk>/`
* **Delete Event:** `/api/events/delete/<int:pk>/`
* **Create Comment:** `/api/events/<int:event_id>/comments/`
* **List Images for Comment:** `/api/comments/<int:comment_id>/images/`

**User Interactions**

* **Express Interest in Event:** `/api/users/<int:user_id>/interests/<int:event_id>/`
* **Remove Interest in Event:** `/api/users/<int:user_id>/interests/<int:event_id>/remove/`
* **Create Group:** `/api/groups/`
* **Get Group Details:** `/api/groups/<int:pk>/`
* **Update Group:** `/api/groups/<int:pk>/update/`
* **Delete Group:** `/api/groups/<int:pk>/delete/`
* **Add Member to Group:** `/api/groups/<int:group_id>/members/<int:user_id>/`
* **Remove Member from Group:** `/api/groups/<int:group_id>/members/<int:user_id>/remove/`

**Authentication**

All endpoints that require authentication require the user to have a valid JSON Web Token (JWT) in the `Authorization` header of the request. The JWT can be obtained by logging in using the `/api/users/login/` endpoint.

**Example**

To create a new event, you would send a POST request to the `/api/events/create/` endpoint with the following JSON body:

```json
{
  "title": "HNGx Event",
  "description": "This is my event description.",
  "start_date": "2023-09-09",
  "end_date": "2023-10-29",
  "location": "Lagos, Nigeria"
}
```

If the request is successful, you will receive a JSON response with the newly created event.

**Error Handling**

All endpoints return a JSON response with a status code and an error message if the request fails. The status code indicates the type of error that occurred, and the error message provides more specific information about the error.

**Conclusion**

This API provides a comprehensive set of endpoints for managing events and users. It is built using Django REST Framework, which makes it easy to use and extend.
