# Multi-User Shared Expense API Specification

## 1. Overview
The Multi-User Shared Expense API is a backend REST API for Campus Split Financial Services. The system will replace the existing isolated, in-memory expense tracker with a centralized backend service using FastAPI, SQLModel, and SQLite.

The API will support user accounts, expense recording, expense splitting, and monthly spending summaries.

## 2. Entity Data Models

### 2.1 User
A User represents a registered roommate or team member.

Fields:

- `id`: unique user identifier and primary key.
- `full_name`: required user's full name.
- `email`: required email address and unique value.

Validation and constraints:

- Each user must have a unique ID.
- Each user must have a unique email address.
- An attempt to register an email that already exists must result in a `409 Conflict`.

### 2.2 Expense
An Expense represents a recorded expense paid by a registered user.

Fields:

- `id`: unique expense identifier and primary key.
- `amount`: exact currency amount using `Decimal` with 2 decimal places.
- `category`: spending category.
- `description`: brief description of the expense.
- `transaction_date`: date the expense occurred.
- `payer_user_id`: identifier of the user who paid the expense.

Validation and constraints:

- The amount must be greater than zero.
- Floating-point `float` values must not be used for money.
- The category must be one of: `food`, `transport`, `utilities`, `entertainment`, or `other`.
- The payer must be an existing user before the expense can be saved.
- Expenses must persist in the SQLite database.

### 2.3 Expense Split
An Expense Split represents the amount owed by an individual participant for an existing expense.

Fields:

- `expense_id`: identifier of the expense being split.
- `participant_user_id`: identifier of the participant user.
- `amount`: exact amount owed by the participant using `Decimal` with 2 decimal places.

Validation and constraints:

- The referenced expense must exist.
- Every participant must be an existing user.
- The split must be performed across the provided participant user IDs.
- The sum of all split amounts must equal the original expense exactly to the cent.
- Any remainder caused by dividing cents must be assigned deterministically to the first participant.

## 3. Relational Invariants
An Expense Split represents the amount owed by an individual participant for an existing expense.

Fields:

- `expense_id`: identifier of the expense being split.
- `participant_user_id`: identifier of the participant user.
- `amount`: exact amount owed by the participant using `Decimal` with 2 decimal places.

Validation and constraints:

- The referenced expense must exist.
- Every participant must be an existing user.
- The split must be performed across the provided participant user IDs.
- The sum of all split amounts must equal the original expense exactly to the cent.
- Any remainder caused by dividing cents must be assigned deterministically to the first participant.

## 4. API Endpoint Contracts

### 4.1 User Endpoints
#### POST /users

Creates a new user account.

Request body:

- `full_name`: string
- `email`: string

Success response:

- `201 Created`
- Returns the newly created user.

Errors:

- `409 Conflict` if the email already exists.
- `422 Unprocessable Entity` if the request fails semantic validation.

#### GET /users

Returns all registered users.

Success response:

- `200 OK`
- Returns a list of users.

#### GET /users/{user_id}

Returns a user profile by ID.

Success response:

- `200 OK`
- Returns the requested user.

Errors:

- `404 Not Found` if the user ID does not exist.


### 4.2 Expense Endpoints

### 4.3 Expense Splitting
#### POST /expenses/{expense_id}/split

Splits an existing expense evenly across a list of participant users.

Request body:

- `participant_user_ids`: list of user IDs

Success response:

- `200 OK`
- Returns the calculated split amounts for each participant.

Rules:

- The expense must already exist.
- Every participant must be an existing user.
- All split amounts must use `Decimal` with 2 decimal places.
- The sum of the split amounts must equal the original expense exactly to the cent.
- Any remaining cent must be assigned to the first participant in the provided participant list.

Errors:

- `404 Not Found` if the expense does not exist.
- `404 Not Found` if a participant user does not exist.
- `422 Unprocessable Entity` if the participant list is invalid.

### 4.4 Monthly Summary
#### GET /reports/monthly/{year}/{month}

Returns spending metrics for a specified year and month.

Parameters:

- `year`: requested year.
- `month`: requested month.

Success response:

- `200 OK`
- Returns:
  - total amount spent during the month
  - spending totals by category
  - category with the highest spending

## 5. Status Code Invariants
| Status Code | Meaning |
|---|---|
| `200 OK` | Successful retrieval or successful operation that does not create a new resource. |
| `201 Created` | Successful resource creation. |
| `400 Bad Request` | Syntactically invalid request payload. |
| `404 Not Found` | Requested entity ID does not exist in storage. |
| `409 Conflict` | Unique constraint violation, such as a duplicate email. |
| `422 Unprocessable Entity` | Semantic validation failure, such as a negative or zero currency amount. |

## 6. Engineering Constraints
### Type Strictness

The project must pass strict mypy checking. Functions must be typed and `Any` must not be used.

### Currency Safety

Floating-point `float` values are strictly prohibited for money. All balances and split amounts must use `Decimal` with 2 decimal places.

### Database Access

The application must use SQLite through SQLModel. Endpoint functions must not contain raw SQL strings.

### Layering

Route endpoints are responsible for HTTP validation and status codes. Business logic must be implemented in the service layer.