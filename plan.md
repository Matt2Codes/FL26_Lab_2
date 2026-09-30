# Multi-User Shared Expense API Technical Plan

## 1. Architecture

The API will use a layered architecture consisting of a presentation/routing layer, a business logic/service layer, and a data storage/model layer.

The application will use FastAPI for the REST API, SQLModel for database models and database access, and SQLite for persistent storage.

The layers will be separated as follows:

- `routers/`: Handles HTTP requests, request validation, and HTTP status codes.
- `services/`: Contains business logic and application rules.
- `models.py`: Defines SQLModel database models and data structures.
- `database.py`: Handles SQLite database configuration and database sessions.
- `main.py`: Creates and configures the FastAPI application.

## 2. Project Structure

The project will use the following file structure:

```
FL26_Lab_2/
├── main.py
├── database.py
├── models.py
├── routers/
│   ├── __init__.py
│   ├── users.py
│   ├── expenses.py
│   └── reports.py
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   ├── expense_service.py
│   └── report_service.py
├── tests/
└── ...
```
'
# 3. Routing Layer

The routing layer will be implemented using FastAPI routers.

Routes will be responsible for:

- Receiving HTTP requests.
- Validating request parameters and request bodies.
- Calling the appropriate service-layer functions.
- Returning the appropriate HTTP status codes and response data.

Routes will not contain business logic or direct database queries.

User-related endpoints will be located in `routers/users.py`.

Expense-related endpoints, including expense splitting, will be located in `routers/expenses.py`.

Monthly reporting endpoints will be located in `routers/reports.py`.

## 4.Service Layer

The service layer will contain the application's business logic.

`services/user_service.py` will handle user-related operations such as creating users and retrieving users.

`services/expense_service.py` will handle expense creation and expense splitting.

`services/report_service.py` will calculate monthly spending summaries and category totals.

The service layer will enforce business rules such as:

- Preventing duplicate user emails.
- Verifying that users exist before creating expenses.
- Verifying participants before splitting an expense.
- Maintaining exact-cent penny invariance when splitting expenses.
- Calculating monthly spending totals and highest-spending categories.

## 5. Data Layer

The data layer will use SQLModel with SQLite.

`models.py` will contain the SQLModel models representing the application's persistent data.

The database will store users, expenses, and expense split information.

`database.py` will configure the SQLite database connection and provide database sessions to the application.

Database operations will be performed through SQLModel rather than raw SQL strings inside endpoint functions.

## 6. Dependency Management

FastAPI dependency injection will be used to provide database sessions to route handlers.

A database session dependency defined in `database.py` will create and provide a SQLModel session for requests that require database access.

The session will be passed from the router to the appropriate service so that database access remains separate from HTTP routing logic.

## 7. Technology Choices

### FastAPI

FastAPI will provide the REST API framework and handle HTTP routing, request validation, and response status codes.

### SQLModel

SQLModel will be used for database models and database operations.

### SQLite

SQLite will provide persistent storage for users, expenses, and expense splits.

### Decimal

Python's `Decimal` type will be used for currency values. Floating-point `float` values will not be used for money.

### mypy

Strict mypy checking will be used to enforce type safety and prevent untyped functions and use of `Any`.