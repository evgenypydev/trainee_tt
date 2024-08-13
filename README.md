
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

When using the token in API requests, ensure to prefix it with Bearer.(example: "Bearer your_access_token")



## API Documentation

The API documentation is available at:

- **Swagger UI**: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)

This provides detailed information about the available endpoints and their parameters.
