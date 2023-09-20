### Event Management System API

This API is built using Django REST Framework and provides a comprehensive set of endpoints for managing events and users.

**Features**

* User management
* Event management
* User interactions

**Authentication**

All endpoints that require authentication require the user to have a valid JSON Web Token (JWT) in the `Authorization` header of the request. The JWT can be obtained by logging in using the `/api/users/login/` endpoint.

**Usage**

To use the API, you will need to send HTTP requests to the appropriate endpoints. The endpoints are all documented in the `documentation.md` file.

**Example**

To create a new event, you would send a POST request to the `/api/events/create/` endpoint with the following JSON body:

```json
{
  "title": "HGNx Event",
  "description": "This is my event description.",
  "start_date": "2023-09-09",
  "end_date": "2023-10-29",
  "location": "Lagos, Nigeria"
}
```

If the request is successful, you will receive a JSON response with the newly created event.

**Error Handling**

All endpoints return a JSON response with a status code and an error message if the request fails. The status code indicates the type of error that occurred, and the error message provides more specific information about the error.

**Documentation**

For more information on how to use the API, please see the `documentation.md` file.

**Contributing**

If you are interested in contributing to the API, please feel free to open a pull request. We welcome all contributions, regardless of size or scope.
