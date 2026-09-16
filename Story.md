Client Requirements Brief: Multi-User Shared Expense API (Lab 2)

Client: Campus Split Financial Services
Target Product: Backend REST API Core  



1. Background & Problem Statement

Our current expense tracking script is an isolated, in-memory prototype running on individual laptops. We need to upgrade this tool into a centralized backend web service backed by a persistent database. 

Your engineering team must translate our business needs into a formal engineering specification (spec.md), design the architecture (plan.md), and construct the API using FastAPI, SQLModel, and SQLite.





2. Business Requirements & Feature Stories



Feature 1: User Accounts & Profiles





Story: As a roommate or team member, I need to register an account so I can participate in shared expenses.



Requirements:





Each user has a unique ID, a full name, and a unique email address.



Attempting to register with an email already on file must be rejected with an appropriate conflict error.



The system must provide a way to look up a user profile by ID and list all registered users.



Feature 2: Recording Expenses





Story: As a user, I want to record an expense that I paid for so that everyone knows what was spent.



Requirements:





An expense must record: an ID, exact currency amount (never negative or zero), spending category, brief description, transaction date, and the payer's user ID.



Allowed categories: food, transport, utilities, entertainment, other.



The system must verify that the user paying the expense actually exists before saving.



Expenses must persist in a database, not disappear when the server restarts.



Feature 3: Expense Splitting & Penny Invariance





Story: As a payer, I want to split a bill evenly across multiple participants so that everyone owes their fair share.



Requirements:





The splitting service takes an existing expense ID and a list of participant user IDs.



All participants must be verified users.



The sum of all individual split amounts MUST equal the original expense down to the exact cent.



If a division creates fractional cents (e.g., $100 split 3 ways is 33.3333...), no fractional money can be lost: two users owe $33.33, and the remainder cent goes deterministically to the first participant ($33.34).



Feature 4: Monthly Summary & Metrics





Story: As a user, I want to see monthly spending reports so I can budget effectively.



Requirements:





Given a specific year and month (e.g., March 2026), the system calculates:





Total amount spent that month.



Total spending broken down by category.



The category with the highest spending.





3. Engineering Constraints





Type Strictness: Strict mypy enforcement (no untyped functions, no Any).



Currency Safety: Floating-point numbers (float) are strictly banned for money. All balances and splits must use decimal.Decimal with 2 decimal places.



Database Access: SQLite via SQLModel. No raw SQL strings inside endpoint functions.



Layering: Route endpoints only handle HTTP validation and status codes; business logic belongs in services.