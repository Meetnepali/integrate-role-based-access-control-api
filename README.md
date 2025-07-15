# Guidance for Task

This project is a modular FastAPI backend focused on secure user profile access within a SaaS context. The goal is to implement robust role-based access control (RBAC) for user profile retrieval endpoints, using established modularity and a custom error response layer.

## Requirements
- Complete the implementation of two key endpoints: viewing your own profile and, as an admin, viewing any user's profile.
- Enforce strict role-based authorization using dependency injection and provided stubs.
- Ensure responses use the correct Pydantic models, and error conditions return structured, consistent error payloads and appropriate HTTP status codes, leveraging the custom exceptions provided.
- Avoid any implementation of authentication, persistence, or UI logic—your focus is on backend access control for the specified endpoints only.
- Only modify the relevant routers, schemas, and exception handling as described; do not introduce architectural changes or modify unrelated features.

## Verifying Your Solution
- You should be able to demonstrate that unauthorized and forbidden access attempts trigger the correct custom error responses, while valid requests from properly authorized users return the appropriate user profile data in the expected schema.
- Valid requests include: a user fetching their own profile, and an admin fetching any user's profile.
- The system should remain modular, easily testable, and use the supplied stub functions and error handling patterns.
