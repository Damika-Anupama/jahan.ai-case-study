## Description

Backend provides APIs for user registration, login, and managing user preferences. JWT authentication is used for secure access.

## Installation Steps
1. Create a virtual environment and activate it:
> python -m venv venv
> source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. Install the dependencies:
> pip install -r requirements.txt

3. Set up the database:
> python manage.py migrate # check with queries.sql

4. Try running commands
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Architecture

Architecture is designed to be modular, scalable, and secure. Below is an overview of the key components and their interactions.

### Components

1. **Models**:
    - `AccountSettings`: Stores user account information such as username, email, and password.
    - `NotificationSettings`: Stores user notification preferences including frequency and types of notifications.
    - `ThemeSettings`: Stores user theme preferences including theme and font size.
    - `PrivacySettings`: Stores user privacy preferences including profile visibility and data sharing options.

2. **Serializers**:
    - `AccountSettingsSerializer`: Serializes and deserializes `AccountSettings` data.
    - `NotificationSettingsSerializer`: Serializes and deserializes `NotificationSettings` data.
    - `ThemeSettingsSerializer`: Serializes and deserializes `ThemeSettings` data.
    - `PrivacySettingsSerializer`: Serializes and deserializes `PrivacySettings` data.

3. **Views**:
    - `RegisterView`: Handles user registration, including creating default settings and generating JWT tokens.
    - `LoginView`: Handles user login and generates JWT tokens.
    - `PreferencesView`: Retrieves user preferences.
    - `UpdatePreferencesView`: Updates user preferences in an atomic transaction.

4. **Authentication**:
    - JWT authentication is used to secure the API endpoints. Tokens are generated upon successful registration and login.

5. **Database**:
    - The backend uses PostgreSQL (or another preferred relational database) to store user data and preferences.

### Data Flow

1. **User Registration**:
    - The user sends a POST request to the `/register/` endpoint with their username, email, and password.
    - The `RegisterView` validates the data, creates the user, sets default preferences, and generates a JWT token.
    - The token is returned in the response.

2. **User Login**:
    - The user sends a POST request to the `/login/` endpoint with their email and password.
    - The `LoginView` authenticates the user and generates a JWT token.
    - The token is returned in the response.

3. **Fetching Preferences**:
    - The user sends a GET request to the `/preferences/` endpoint with their JWT token.
    - The `PreferencesView` retrieves the user's preferences and returns them in the response.

4. **Updating Preferences**:
    - The user sends a PATCH request to the `/preferences/<section>/` endpoint with their JWT token and the updated data.
    - The `UpdatePreferencesView` validates the data, updates the preferences in an atomic transaction, and returns the updated data in the response.

### Error Handling

- Robust validation and error handling mechanisms are implemented to ensure data integrity and provide meaningful error messages.
- Common errors include invalid credentials, missing data, and invalid section names.

### Security

- JWT tokens are used to secure API endpoints and ensure that only authenticated users can access their preferences.

### Testing

- Unit and functional tests are written to ensure the proper functionality of the views.
- Tests cover user registration, login, fetching preferences, and updating preferences.
