# Multi-User Shared Expense API Implementation Tasks

Each task represents one discrete feature or implementation unit. Each task should be completed on its own Git feature branch.

A task is only considered complete after the required automated checks pass:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 1 — Database Setup

Set up the SQLite database and SQLModel database session management.

Branch:

`feat/task-1-database-setup`

Work includes:

- Configure the SQLite database.
- Create the database engine.
- Create the database session dependency.
- Configure database table creation.

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 2 — User Model

Create the SQLModel User model.

Branch:

`feat/task-2-user-model`

Work includes:

- Create the user ID field.
- Create the full name field.
- Create the email field.
- Enforce the unique email requirement.

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 3 — User Service

Implement the business logic for creating and retrieving users.

Branch:

`feat/task-3-user-service`

Work includes:

- Create a new user.
- Reject duplicate email addresses.
- Retrieve a user by ID.
- Retrieve all users.

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 4 — User Routes

Implement the FastAPI user endpoints defined in `spec.md`.

Branch:

`feat/task-4-user-routes`

Work includes:

- `POST /users`
- `GET /users`
- `GET /users/{user_id}`
- Map service results and errors to the appropriate HTTP status codes.

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 5 — Expense Model

Create the SQLModel Expense model.

Branch:

`feat/task-5-expense-model`

Work includes:

- Expense ID.
- Decimal currency amount.
- Category.
- Description.
- Transaction date.
- Payer user ID.
- Relationship to the payer user.

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 6 — Expense Service

Implement the business logic for creating expenses.

Branch:

`feat/task-6-expense-service`

Work includes:

- Validate that the payer exists.
- Validate that the amount is greater than zero.
- Validate the allowed expense categories.
- Store the expense in SQLite.
- Ensure currency values use Decimal with two decimal places.

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 7 — Expense Routes

Implement the expense creation endpoint defined in `spec.md`.

Branch:

`feat/task-7-expense-routes`

Work includes:

- `POST /expenses`
- Request validation.
- Calling the expense service.
- Returning the appropriate HTTP status codes.

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 8 — Expense Splitting

Implement the expense splitting business logic and endpoint.

Branch:

`feat/task-8-expense-splitting`

Work includes:

- Verify that the expense exists.
- Verify that every participant exists.
- Divide the expense evenly.
- Use Decimal for all currency calculations.
- Preserve the exact original amount down to the cent.
- Assign any remaining cent to the first participant.

Endpoint:

`POST /expenses/{expense_id}/split`

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 9 — Monthly Reports

Implement the monthly spending summary functionality.

Branch:

`feat/task-9-monthly-reports`

Work includes:

- Calculate total spending for a specified year and month.
- Calculate spending totals by category.
- Determine the highest-spending category.
- Implement the monthly report endpoint.

Endpoint:

`GET /reports/monthly/{year}/{month}`

Verification:

- `pytest`
- `ruff check`
- `mypy --strict`

## Task 10 — Final Integration and Verification

Verify that the complete API follows the requirements in `spec.md` and the architecture in `plan.md`.

Branch:

`feat/task-10-final-verification`

Verification:

- Run `pytest` with all tests passing.
- Run `ruff check` with zero errors.
- Run `mypy --strict` with zero errors.
- Verify that no `float` values are used for currency.
- Verify that route handlers do not contain business logic.
- Verify that database operations use SQLModel and SQLite.