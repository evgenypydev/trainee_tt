
# Trainee TT Project

## Description

This project is a RESTful web service built with Django and Django REST Framework (DRF). It provides an API for managing posts and users, with JWT (JSON Web Token) authentication for security.

## Key Features

- **Public Posts**: Available to all users, including unauthenticated ones.
- **Private Posts**: Accessible only to authenticated users with the "subscriber" role.
- **Post Management**: Creating, editing, and deleting posts is restricted to users with the "author" role.
- **User Registration**: New users can register with the "subscriber" role.
- **Authentication**: User authentication is handled via JWT.

## Running the Project

### Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose

### Running the Project with Docker

1. **Clone the repository**:

    ```bash
    git clone https://github.com/evgenypydev/trainee_tt.git
    cd trainee_tt
    ```

2. **Rename the environment file**:

    Rename the `.env.dev` file to `.env` in the root of the project.

3. **Start the project**:

    Run the following command to build and start the containers:

    ```bash
    docker compose up -d
    ```

The application will be up and running with the database migrations automatically applied. You do not need to run additional commands to apply migrations or create a superuser.

### Stopping the Project

To stop and remove the running containers, use:

```bash
docker compose down
```

## API Usage

### Authentication

To perform secured operations (such as creating, editing, and deleting posts), you need to authenticate using a Bearer Token.

1. **Obtain a token**:

    Send a POST request to `/api/token/` with the user's email and password:

    ```bash
    curl -X POST -d "email=user@example.com&password=password" http://localhost:8000/api/token/
    ```

2. **Using the token**:

    Include the obtained token in the `Authorization` header of your requests as follows:

    ```
    Authorization: Bearer your_access_token
    ```

    Example request with the token:

    ```bash
    curl -H "Authorization: Bearer your_access_token" http://localhost:8000/api/posts/
    ```

## Logging

User actions are logged using an Access Token (Bearer Token). Ensure the token is correctly passed in the `Authorization` header.

## API Documentation

The API documentation is available at:

- **Swagger UI**: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)

This provides detailed information about the available endpoints and their parameters.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
